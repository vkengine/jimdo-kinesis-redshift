initialize:
	aws configure

build:
	terraform apply -var-file="build.tfvars" --auto-approve

destroy-infra:
	terraform destroy -var-file="build.tfvars" --auto-approve

create-infra:
	terraform init
	@echo "Listing resoruces to be created"
	terraform plan -var-file="build.tfvars"
	@echo -n "Are you sure you want to create environment? [y/N] " && read ans && if [ $${ans:-'N'} = 'y' ]; then make build; fi

destroy:
	@echo -n "Are you sure you want to destroy environment? [y/N] " && read ans && if [ $${ans:-'N'} = 'y' ]; then make destroy-infra; fi

dump-dummy-data:
	python ./lambda/write_to_k_stream.py