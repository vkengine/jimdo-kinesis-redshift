initialize:
	aws configure

build:
	terraform apply --auto-approve

destroy:
	terraform destroy --auto-approve

create-infra:
	terraform init
	@echo "Listing resoruces to be created"
	terraform plan
	@echo -n "Are you sure you want to create environment? [y/N] " && read ans && if [ $${ans:-'N'} = 'y' ]; then make build; fi

destroy-infra:
	@echo -n "Are you sure you want to create environment? [y/N] " && read ans && if [ $${ans:-'N'} = 'y' ]; then make destroy; fi

dump-dummy-data:
	python ./lambda/write_to_k_stream.py