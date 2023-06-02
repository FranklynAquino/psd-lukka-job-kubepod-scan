import argparse
from typing import List
from myUtils import (env, get_logger)
from api.process.opensearch_endpoints import OpenSearchEndpoints
from api.opensearch_response_object import OpenSearchResponseObject
from api.my_objects.job_id_list_object import JobIdListObject


logger = get_logger('Main Run')

parser = argparse.ArgumentParser()
parser.add_argument('job_id_list', 
                    nargs='?',
                    help='Insert path for Job ID list',
                    default='')
args = parser.parse_args()
job_id_list_filename = f'{args.job_id_list}'

opensearch = OpenSearchEndpoints(env.opensearch_host_name, env.opensearch_port_number, 
                        env.opensearch_username, env.opensearch_password)

opensearch_response_list:List[OpenSearchResponseObject] = []

with open(f'{job_id_list_filename}') as file1:
    file1_content = file1.readlines()
    for content in file1_content:
        try:
            j_object = JobIdListObject(job_id=content)
            opensearch.set_payload(arg1=j_object.job_id,
                                    mins_before = 3000,
                                    opensearch_search_type='phrase')
            search_response:dict = opensearch.run_search(size=1,filter=['hits.hits._source'])
            hits = search_response['hits']['hits']
            logger.info(f' hits-> {hits}')
        except KeyError as e:
            logger.info(f'No hits found. Key Error -> {e}')
            pass

        try:
            for hit in hits:
                if any(x for x in hit['_source']):
                        logger.info(f'Serializing hits from response')
                        opensearch_response:OpenSearchResponseObject = OpenSearchResponseObject(label_app_name=hit['_source']['kubernetes']['labels']['app'],
                                                                                                pod_name=hit['_source']['kubernetes']['pod_name'],
                                                                                                public_ip=hit['_source']['log_processed']['publicIP'],
                                                                                                job_id=j_object.job_id)
                        opensearch_response_list.append(opensearch_response)
        except KeyError as e:
            logger.info(f'KeyError found -> {e}')
            pass
        except NameError as e:
            logger.info(f'Key Error Found -> {e}')
            pass
        
for response in opensearch_response_list:
    logger.info(f'{response.to_string()}')