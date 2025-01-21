/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // root_directory/templates/home.html
    // root_directory/templates/subdirectory/home.html
    './templates/**/*.html',

    // root_directory/app_name/templates/app_name/home.html
    // root_directory/otherapp/templates/otherapp/index.html

    './**/templates/**/*.html',
],
  theme: {
    extend: {},
  },
  daisyui: {
    themes: ["halloween", "night"],
  },
  plugins: [require('daisyui'),],
}

