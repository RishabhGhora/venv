from setuptools import setup, find_packages

if __name__ == '__main__':
  bt_required_packages = open('bt_required_packages.req').read().splitlines()
  third_party_required_packages = open('third_party_required_packages.req').read().splitlines()

  require_packages = third_party_required_packages + bt_required_packages

setup(name='TradeManager',
      version='0.0.1',
      author='Belvedere',
      author_email='release_group@belvederetrading.com',
      packages=find_packages(),
      package_data={'TradingManager': []},
      url='http://pypi:28080/simple/TradeManager',
      license='LICENSE.txt',
      description='Rishabh Ghora BTU Dev 101 Python HW',
      long_description=open('README.rst').read(),
      install_requires=require_packages,
      classifiers=['BtPython :: Module'],
      tests_require=['mock'])