
process.chdir('marathon-code/docs/docs/rest-api/public/api')
var slConverter = require('api-spec-converter'), //Warning: not published to npm yet
    fs = require('fs')
ramlToSwaggerConverter = new slConverter.Converter(slConverter.Formats.RAML, slConverter.Formats.SWAGGER)
ramlToSwaggerConverter.loadFile('api.raml', function(err){
  if (err) {
    console.log(err.stack);
    return;
  }

  ramlToSwaggerConverter.convert('yaml')
  .then(function(convertedData){
    fs.writeFileSync('../../../../../../swagger.yaml', convertedData, 'utf8');
  })
  .catch(function(err){
    console.log(err);
  })
});
