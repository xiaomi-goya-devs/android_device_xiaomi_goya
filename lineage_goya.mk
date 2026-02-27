#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from the custom device configuration.
$(call inherit-product, device/xiaomi/goya/device.mk)

# Inherit from the LineageOS configuration.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_BRAND := Xiaomi
PRODUCT_DEVICE := goya
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_MODEL := 25069PTEBG
PRODUCT_NAME := lineage_goya

PRODUCT_BRAND_FOR_ATTESTATION := $(PRODUCT_BRAND)
PRODUCT_DEVICE_FOR_ATTESTATION := $(PRODUCT_DEVICE)
PRODUCT_MODEL_FOR_ATTESTATION := $(PRODUCT_MODEL)
PRODUCT_NAME_FOR_ATTESTATION := goya_eea
PRODUCT_MANUFACTURER_FOR_ATTESTATION := $(PRODUCT_MANUFACTURER)

PRODUCT_CHARACTERISTICS := nosdcard
PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="missi-user 16 BP2A.250605.031.A3 OS3.0.10.0.WOEEUXM release-keys" \
    BuildFingerprint=Xiaomi/goya_eea/goya:16/BP2A.250605.031.A3/OS3.0.10.0.WOEEUXM:user/release-keys \
    DeviceName=goya \
    DeviceProduct=goya_eea \
    SystemDevice=goya \
    SystemName=goya_eea
