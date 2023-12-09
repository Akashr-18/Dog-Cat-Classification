from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = 'Data Ingestion stage'
try:
    logger.info(f'>>>>>>> Stage1 {STAGE_NAME} started <<<<<<<')
    data_ingestion_obj = DataIngestionTrainingPipeline()
    data_ingestion_obj.main()
    logger.info(f'>>>>>>> Stage1 {STAGE_NAME} completed <<<<<<<')
        
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Preapre Base Model stage'
try:
    logger.info(f'*' * 100 )
    logger.info(f'>>>>>>> Stage2 {STAGE_NAME} started <<<<<<<')
    prepare_base_model_obj = PrepareBaseModelTrainingPipeline()
    prepare_base_model_obj.main()
    logger.info(f'>>>>>>> Stage2 {STAGE_NAME} completed <<<<<<<')

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Training stage'
try:
    logger.info(f'*' * 100 )
    logger.info(f'>>>>>>> Stage3 {STAGE_NAME} started <<<<<<<')
    training_obj = ModelTrainingPipeline()
    training_obj.main()
    logger.info(f'>>>>>>> Stage3 {STAGE_NAME} completed <<<<<<<')

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation stage"
try:
   logger.info(f'*' * 100 )
   logger.info(f">>>>>> stage4 {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage4 {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e
