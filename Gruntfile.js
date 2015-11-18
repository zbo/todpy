module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    react: {
      single_file_output: {
        files: {
          '/web/web/static/react/build/feature-container.js': '/web/web/static/react/auto/feature-container.jsx'
        }
      },
      combined_file_output: {
        files: {
          'path/to/output/dir/combined.js': [
            'path/to/jsx/templates/dir/input1.jsx',
            'path/to/jsx/templates/dir/input2.jsx'
          ]
        }
      },
      dynamic_mappings: {
          files: [
          {
            expand: true,
            cwd: 'web/web/static/react',
            src: ['**/*.jsx'],
            dest: 'web/web/static/react/build/',
            ext: '.js'
          }
        ]
      }
    },
    dist: {
      files: {
          '../js/<%= pkg.name %>.js': ['js/build/*.js', 'js/base.js'],
      },
      options: {
          transform: [ require('grunt-react').browserify ]
      }
    }
  })

  grunt.loadNpmTasks('grunt-react');
  grunt.loadNpmTasks('grunt-browserify');

  grunt.registerTask('build', function(target){
    grunt.task.run([
      'react:dynamic_mappings'
    ]);
  });
};