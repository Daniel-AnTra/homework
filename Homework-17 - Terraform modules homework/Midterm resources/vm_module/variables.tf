variable "base_name" {
  type = string
  default = "vmtask"
}
variable "location" {
  type = string
  default = "eastus"
}
variable "my_public_ip"{
    type = string
    default = "77.29.137.204"
}
variable "my_password" {
  type = string
  default = "Adminpassword123!"
}
variable "vms_subnet_id"{
    type = string 
    default =  "10.0.1.0/24"
}