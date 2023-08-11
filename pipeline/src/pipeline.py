import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import argparse

import logging

from src.other_file import pandas_tester
from examplelib.example import add
# test import lib



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--number_to_add", type=int, default=10)
    parser.add_argument("--skip_step", default="no")
    args, beam_args = parser.parse_known_args()
    pipeline_options = PipelineOptions(beam_args, save_main_session=True, sdk_location="container")
    # test flex template with parameters / different graph
    with beam.Pipeline(options=pipeline_options) as p:
        input = (p   | beam.Create([1, 2, 3, 4, 5]))

        if args.skip_step == "yes":
                (input
                    | beam.Map(add, args.number_to_add)
                    | beam.Map(print)
                )
        elif args.skip_step == "no":
                (input
                    | beam.Map(pandas_tester)
                    | beam.Map(add, args.number_to_add)
                    | beam.Map(print)
                )



if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    main()