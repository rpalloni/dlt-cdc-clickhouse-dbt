import dlt
import time
from dlt.sources.filesystem import filesystem, read_jsonl

POLL_INTERVAL = 5

def bucket_to_clickhouse() -> None:
    """Continuously poll MinIO and ingest new event files into ClickHouse"""
    pipeline = dlt.pipeline(
        pipeline_name="bucket_to_clickhouse",
        destination="clickhouse",
        dataset_name="events"
    )

    print(f'Polling s3://events/**/*.jsonl every {POLL_INTERVAL} sec - Ctrl+C to stop')

    while True:
        source = (
            filesystem(
                bucket_url="s3://events",
                file_glob="**/*.jsonl",
                incremental=dlt.sources.incremental("modification_date")
            ) | read_jsonl()
        )

        load_info = pipeline.run(source, table_name="events", write_disposition="append")

        # monitoring
        n_jobs = sum(len(pkg.jobs.get("completed_jobs", [])) for pkg in load_info.load_packages)
        if n_jobs:
            print(f'Loaded {n_jobs} files(s) loads={load_info.loads_ids}')
        else:
            print('.', end='', flush=True)

        time.sleep(POLL_INTERVAL)

if __name__ == '__main__':
    bucket_to_clickhouse()