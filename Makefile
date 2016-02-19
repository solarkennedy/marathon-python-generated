#marathon-python-generated: ./node_modules/.bin/raml2swagger marathon-code/.git
#	./node_modules/.bin/raml2swagger marathon-code/docs/docs/rest-api/public/api/api.raml

#node_modules/.bin/raml2swagger:
#	npm install raml-to-swagger

swagger.yaml:
	node convert.js

node_modules/api-spec-converter/:
	npm install git+https://github.com/stoplightio/api-spec-converter.git

marathon-code/.git:
	git clone https://github.com/mesosphere/marathon.git marathon-code

clean:
	rm -rf node_modules marathon-code
