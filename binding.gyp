{
  'targets': [
    {
      'target_name': 'memwatch',
      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ],
      'sources': [
        'src/heapdiff.cc',
        'src/init.cc',
        'src/memwatch.cc',
        'src/util.cc'
      ],
      'conditions': [
        ['OS=="android"', {
          'cflags_cc': ['-std=c++11',' -Wall','-O3',' -fPIC']
        }]
      ]
    }
  ]
}
