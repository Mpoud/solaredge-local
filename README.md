# SolarEdge Local

The goal if this respository is to provide information about using the local API available on some solar edge inverters.  This is a WIP based on my observations and may contain inaccuracies.  Pull Requests or Issues are encouraged to correct any mistakes or add additonal informatoin.

### Relevant Models

The local api appears to be available on the [SExxxxH-US models with SetApp](https://www.solaredge.com/sites/default/files/se-hd-wave-single-phase-inverter-with-setapp-datasheet-na.pdf).  See [more information on SetApp](https://www.solaredge.com/us/products/installer-tools/setapp). These models have no LED screen, and are provisioned via a phone app when installed.

You can check by finding the IP address of your inverter and visiting it in a browser.  If it supports the local API, you'll see the SolarEdge logo and a "Commissioning" menu.

### API Endpoints

AppConfigs: "web/v1/app_configs",
Region: "web/v1/region",
Region_Country: "web/v1/region/country",
Region_Language: "web/v1/region/language",
Pairing: "web/v1/pairing",
Pairing_Request: "web/v1/pairing/request",
Communication: "web/v1/communication",
Communication_Server: "web/v1/communication/server",
Communication_Lan: "web/v1/communication/lan",
Communication_Rs485_SlaveDetect: "web/v1/communication/rs485/<id>/slave_detect",
Communication_Rs485_Protocol: "web/v1/communication/rs485/<id>/protocol",
Communication_Rs485_DeviceId: "web/v1/communication/rs485/<id>/deviceid",
Communication_Rs485_Modbus: "web/v1/communication/rs485/<id>/modbus",
Communication_Rs485_Modbus_AddDevice: "web/v1/communication/rs485/<id>/modbus/add_device",
Communication_Rs485_Modbus_RemoveDevice: "web/v1/communication/rs485/<id>/modbus/remove_device",
Communication_Wifi: "web/v1/communication/wifi",
Communication_Wifi_Wps: "web/v1/communication/wifi/wps",
Communication_Wifi_Connect: "web/v1/communication/wifi/connect",
Communication_Cellular: "web/v1/communication/cellular",
Communication_Zigbee_Defaults: "web/v1/communication/zigbee/defaults",
Communication_Zigbee_ModuleConfigs: "web/v1/communication/zigbee/module_configs",
Communication_Zigbee_OpMode: "web/v1/communication/zigbee/op_mode",
Communication_Gpio_Pri: "web/v1/communication/gpio/pri",
Communication_ModbusTcp: "web/v1/communication/modbus_tcp",
PowerControl: "web/v1/power_control",
PowerControl_GridControl: "web/v1/power_control/grid_control",
PowerControl_EnergyManager_LimitControl: "web/v1/power_control/energy_manager/limit_control",
PowerControl_EnergyManager_EnergyControl: "web/v1/power_control/energy_manager/energy_control",
PowerControl_EnergyManager_StorageControl: "web/v1/power_control/energy_manager/storage_control",
PowerControl_ReactivePower: "web/v1/power_control/reactive_power",
PowerControl_ActivePower: "web/v1/power_control/active_power",
PowerControl_Wakeup: "web/v1/power_control/wakeup",
PowerControl_Advanced: "web/v1/power_control/advanced",
PowerControl_Reset: "web/v1/power_control/reset",
PowerControl_Rrcr: "web/v1/power_control/rrcr",
Maintenance: "web/v1/maintenance",
Maintenance_DateTime: "web/v1/maintenance/date_and_time",
Maintenance_ResetCounters: "web/v1/maintenance/reset_counters",
Maintenance_ResetFactory: "web/v1/maintenance/reset_factory",
Maintenance_Afci: "web/v1/maintenance/afci",
Maintenance_AfciTest: "web/v1/maintenance/afci/test",
Maintenance_Inverters_SelfTest: "web/v1/maintenance/inverters/<position>/self_test",
Maintenance_Standby: "web/v1/maintenance/standby",
Maintenance_GridProtectionLogin: "web/v1/maintenance/grid_protection/login",
Maintenance_GridProtection: "web/v1/maintenance/grid_protection",
Maintenance_UpgradeUsb: "web/v1/maintenance/fw_upgrade/usb",
Information: "web/v1/information",
Status: "web/v1/status",
Status_ServerCommTest: "web/v1/status/server_comm_test"

### Using the API

All endpoints I have explored so far appear to be a GET, and responses use [Protocol Buffers](https://developers.google.com/protocol-buffers/).  There is no authentication

You can see the raw data by doing the following (assuming you have the protoocal buffers CLI tool installed)

```
curl http://<inverter ip>/web/v1/status --output response.bin
protoc --decode_raw < response.bin
```

Many numbers appear to be 32 bit floating point.

The proto definitions required to fully parse the responses are available in  javascript if you choose "view source" in the developer tools of your browser.
