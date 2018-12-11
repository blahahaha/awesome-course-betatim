
test = {
  'name': 'test_valid',
  'points': 1,
  'suites': [
    {
      'cases': [
      {'code': r"""
>>> res = xtimesy(3, -2)
>>> assert res == 6, "3 times -2 should also equal 6, not {}".format(res)
                    """,
                    'points': 4},
{'code': r"""
>>> res = xtimesy(3, -2)
>>> assert res == 6-1, "3 times -2 should also equal 6, not {}".format(res)
                    """,
                    'points': 2},
      ]
    }
  ]
}
