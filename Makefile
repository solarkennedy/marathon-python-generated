#marathon-python-generated: ./node_modules/.bin/raml2swagger marathon-code/.git
#	./node_modules/.bin/raml2swagger marathon-code/docs/docs/rest-api/public/api/api.raml

#node_modules/.bin/raml2swagger:
#	npm install raml-to-swagger
marathon-python-generated: swagger-codegen-cli.jar marathon-code/.git marathon-raml.yaml swagger.json
	/usr/lib/jvm/java-8-oracle-1.8.0.45/bin/java -jar swagger-codegen-cli.jar generate -l python -i swagger.json -o marathon-python-generated

swagger-codegen-cli.jar:
	wget http://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.1.5/swagger-codegen-cli-2.1.5.jar -O swagger-codegen-cli.jar

marathon-raml.yaml: node_modules/api-spec-converter/
	node convert.js

swagger.json:
	echo "Go to https://apitransformer.com/#convert"
	echo "and save it as swagger.json"
	exit 1

node_modules/api-spec-converter/:
	npm install git+https://github.com/stoplightio/api-spec-converter.git

marathon-code/.git:
	git clone https://github.com/mesosphere/marathon.git marathon-code

clean:
	rm -rf node_modules marathon-code
