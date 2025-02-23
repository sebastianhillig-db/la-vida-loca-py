from setuptools import setup

setup(
    name='la-vida-local',
    version='1.5.11',
    install_requires = [
      #'cloudpickle==1.6.0',
      #'protobuf',
      #'requests',
    ],
    extras_require = {
      #"grpc": ["grpclib", "pyarrow", "grpcio"]
    },
    packages=[
      'pyspark',
      'pyspark.cloudpickle',
      'pyspark.sql',
      'pyspark.sql.connect',
      'pyspark.sql.connect.proto'],
)