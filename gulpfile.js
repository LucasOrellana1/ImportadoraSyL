const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));

function compilarSass() {
    return gulp.src('src/scss/app.scss') // Ruta de tu archivo principal SCSS
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('main/static/css')) // Ruta de salida en la raíz del proyecto
}

function observarCambios() {
    gulp.watch('src/scss/**/*.scss', compilarSass); // Observa cambios en los archivos SCSS
}

exports.compilarSass = compilarSass;
exports.observarCambios = observarCambios;