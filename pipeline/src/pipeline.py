import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import argparse


# test import lib

def add_one(x):
    # test pandas in here
    return x + 1

def main():
    parser = argparse.ArgumentParser()
    args, beam_args = parser.parse_known_args()
    pipeline_options = PipelineOptions(beam_args, save_main_session=True, sdk_location="container")
    # test flex template with parameters / different graph
    with beam.Pipeline(options=pipeline_options) as p:
        (
            p   | beam.Create([1, 2, 3, 4, 5])
                | beam.Map(add_one)
                | beam.Map(print)
        )

if __name__ == '__main__':
    main()