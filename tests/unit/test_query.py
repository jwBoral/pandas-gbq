
import pkg_resources

try:
    import mock
except ImportError:  # pragma: NO COVER
    from unittest import mock

from pandas_gbq import query


@mock.patch('google.cloud.bigquery.QueryJobConfig')
def test_query_config_w_old_bq_version(mock_config):
    old_version = pkg_resources.parse_version('0.29.0')
    query.query_config({'query': {'useLegacySql': False}}, old_version)
    mock_config.from_api_repr.assert_called_once_with({'useLegacySql': False})


@mock.patch('google.cloud.bigquery.QueryJobConfig')
def test_query_config_w_dev_bq_version(mock_config):
    dev_version = pkg_resources.parse_version('0.32.0.dev1')
    query.query_config(
        {
            'query': {
                'useLegacySql': False,
            },
            'labels': {'key': 'value'},
        },
        dev_version)
    mock_config.from_api_repr.assert_called_once_with(
        {
            'query': {
                'useLegacySql': False,
            },
            'labels': {'key': 'value'},
        })


@mock.patch('google.cloud.bigquery.QueryJobConfig')
def test_query_config_w_new_bq_version(mock_config):
    dev_version = pkg_resources.parse_version('1.0.0')
    query.query_config(
        {
            'query': {
                'useLegacySql': False,
            },
            'labels': {'key': 'value'},
        },
        dev_version)
    mock_config.from_api_repr.assert_called_once_with(
        {
            'query': {
                'useLegacySql': False,
            },
            'labels': {'key': 'value'},
        })
