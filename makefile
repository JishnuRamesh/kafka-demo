# Other config
NO_COLOR=\033[0m
OK_COLOR=\033[32;01m
ERROR_COLOR=\033[31;01m
WARN_COLOR=\033[33;01m


dev-up:
	@echo "$(OK_COLOR)==> Running docker-compose up$(NO_COLOR)"
	@docker-compose up -d
	@echo "$(OK_COLOR)==> Wait a bit to apply avro schemas for Kafka$(NO_COLOR)"
	@sleep 20
	@./dev/apply-avro-schemas.sh

