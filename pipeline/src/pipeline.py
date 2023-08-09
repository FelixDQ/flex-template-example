import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import argparse
import pandas as pd

# test import lib

def pandas_tester(x):
    df = pd.DataFrame([x])
    df = df * 2
    return df[0].item()

def main():
    parser = argparse.ArgumentParser()
    args, beam_args = parser.parse_known_args()
    pipeline_options = PipelineOptions(beam_args, save_main_session=True, sdk_location="container")
    # test flex template with parameters / different graph
    with beam.Pipeline(options=pipeline_options) as p:
        (
            p   | beam.Create([1, 2, 3, 4, 5])
                | beam.Map(pandas_tester)
                | beam.Map(print)
        )


if __name__ == '__main__':
    main()