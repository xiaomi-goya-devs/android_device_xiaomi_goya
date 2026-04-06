#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.file import File
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/goya',
    'hardware/mediatek',
    'hardware/xiaomi',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'libneuron_graph_delegate.mtk',
        'libnir_neon_driver_ndk.mtk.vndk',
        'libtflite_mtk',
        'vendor.mediatek.hardware.apuware.apusys-V5-ndk',
        'vendor.mediatek.hardware.apuware.utils-V1-ndk',
        'vendor.mediatek.hardware.apuware.utils@2.0',
        'vendor.mediatek.hardware.neuropilot.agent-V1-ndk',
        'vendor.mediatek.hardware.videotelephony-V1-ndk'
    ): lib_fixup_vendor_suffix,
}


blob_fixups: blob_fixups_user_type = {
    (
        'odm/lib64/libTrueSight.so',
        'odm/lib64/libMiVideoFilter.so',
        'vendor/lib64/mt6899/libneuralnetworks_sl_driver_mtk_prebuilt.so'
    ): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_createFromHandle')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_getNativeHandle')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    'system_ext/lib64/libimsma.so': blob_fixup()
        .replace_needed('libsink.so', 'libsink-mtk.so'),
    (
        'vendor/bin/mnld',
        'vendor/lib64/mt6899/libaalservice.so',
        'vendor/lib64/mt6899/libpqconfig.so'
    ): blob_fixup()
        .replace_needed('android.hardware.sensors-V2-ndk.so', 'android.hardware.sensors-V3-ndk.so'),
    'vendor/bin/hw/android.hardware.audio.service-aidl.mediatek': blob_fixup()
        .replace_needed('android.hardware.audio.core-V2-ndk.so', 'android.hardware.audio.core-V3-ndk.so')
        .replace_needed('android.hardware.audio.core.sounddose-V2-ndk.so', 'android.hardware.audio.core.sounddose-V3-ndk.so')
        .replace_needed('android.hardware.bluetooth.audio-V4-ndk.so', 'android.hardware.bluetooth.audio-V5-ndk.so')
        .replace_needed('android.hardware.soundtrigger3-V2-ndk.so', 'android.hardware.soundtrigger3-V3-ndk.so')
        .replace_needed('libaudio_aidl_conversion_common_ndk.so', 'libaudio_aidl_conversion_common_ndk_prebuilt.so'),
    (
        'vendor/bin/hw/mt6899/android.hardware.graphics.allocator-V2-service-mediatek.mt6899',
        'vendor/lib64/egl/mt6899/libGLES_mali.so',
        'vendor/lib64/hw/mt6899/android.hardware.graphics.allocator-V2-mediatek.so',
        'vendor/lib64/hw/mt6899/mapper.mediatek.so',
        'vendor/lib64/mt6899/libmtkcam_grallocutils.so',
        'vendor/lib64/libcodec2_fsr.so',
        'vendor/lib64/libcodec2_vpp_AIMEMC_plugin.so',
        'vendor/lib64/libcodec2_vpp_AISR_plugin.so',
        'vendor/lib64/libgpud.so',
        'vendor/lib64/libmtkcam_grallocutils_aidlv2helper.so',
        'vendor/lib64/vendor.mediatek.hardware.camera.isphal-V1-ndk.so',
        'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V2-ndk.so',
        'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V4-ndk.so',
        'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V7-ndk.so'
    ): blob_fixup()
        .replace_needed('android.hardware.graphics.common-V5-ndk.so', 'android.hardware.graphics.common-V7-ndk.so'),
    'vendor/lib64/hw/android.hardware.audio.effect.aidl-impl-mediatek.so': blob_fixup()
        .replace_needed('android.hardware.audio.effect-V2-ndk.so', 'android.hardware.audio.effect-V3-ndk.so'),
    'vendor/lib64/hw/audio.primary.mediatek.so': blob_fixup()
        .replace_needed('android.hardware.audio.effect-V2-ndk.so', 'android.hardware.audio.effect-V3-ndk.so')
        .replace_needed('android.hardware.audio.common-V1-ndk.so', 'android.hardware.audio.common-V4-ndk.so')
        .replace_needed('android.hardware.bluetooth.audio-V4-ndk.so', 'android.hardware.bluetooth.audio-V5-ndk.so'),
    'vendor/lib64/hw/android.hardware.soundtrigger3-impl.so': blob_fixup()
        .replace_needed('android.hardware.soundtrigger3-V2-ndk.so', 'android.hardware.soundtrigger3-V3-ndk.so')
        .replace_needed('libaudio_aidl_conversion_common_ndk.so', 'libaudio_aidl_conversion_common_ndk_prebuilt.so'),
    (
        'vendor/lib64/hw/hwcomposer.mtk_common.so',
        'vendor/lib64/mt6899/libmtkcam_taskmgr.so'
    ): blob_fixup()
        .add_needed('libprocessgroup_shim.so'),
    (
        'vendor/lib64/soundfx/libaecsw_mtk.so',
        'vendor/lib64/soundfx/libagc1sw_mtk.so',
        'vendor/lib64/soundfx/libagc2sw_mtk.so',
        'vendor/lib64/soundfx/libnssw_mtk.so',
        'vendor/lib64/soundfx/libpreprocessingaidl_mtk.so',
    ): blob_fixup()
        .replace_needed('android.hardware.audio.effect-V2-ndk.so', 'android.hardware.audio.effect-V3-ndk.so')
        .replace_needed('android.media.audio.common.types-V5-ndk.so', 'android.media.audio.common.types-V4-ndk.so'),
    'vendor/lib64/mt6899/libneuron_adapter_mgvi.so': blob_fixup()
        .clear_symbol_version('AHardwareBuffer_describe'),
    'vendor/lib64/android.hardware.audio.core-impl-mediatek.so': blob_fixup()
        .add_needed('libaudioutils_shim.so')
        .replace_needed('android.hardware.audio.core.sounddose-V2-ndk.so', 'android.hardware.audio.core.sounddose-V3-ndk.so')
        .replace_needed('android.hardware.audio.core-V2-ndk.so', 'android.hardware.audio.core-V3-ndk.so')
        .replace_needed('android.hardware.bluetooth.audio-V4-ndk.so', 'android.hardware.bluetooth.audio-V5-ndk.so')
        .replace_needed('libaudio_aidl_conversion_common_ndk.so', 'libaudio_aidl_conversion_common_ndk_prebuilt.so'),
    (
        'vendor/lib64/android.hardware.bluetooth.audio-impl-mediatek.so',
        'vendor/lib64/libbluetooth_audio_session_aidl_mtk.so'
    ): blob_fixup()
        .replace_needed('android.hardware.bluetooth.audio-V4-ndk.so', 'android.hardware.bluetooth.audio-V5-ndk.so'),
    'vendor/lib64/libaudioprimarydevicehalifclient.so': blob_fixup()
        .replace_needed('android.hardware.audio.core-V2-ndk.so', 'android.hardware.audio.core-V3-ndk.so'),
    'vendor/lib64/vendor.mediatek.hardware.bluetooth.audio-V1-ndk.so': blob_fixup()
        .replace_needed('android.hardware.audio.common-V3-ndk.so', 'android.hardware.audio.common-V4-ndk.so'),
    'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V7-ndk.so': blob_fixup()
        .replace_needed('android.hardware.graphics.common-V4-ndk.so', 'android.hardware.graphics.common-V7-ndk.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'goya',
    'xiaomi',
    add_firmware_proprietary_file=True,
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
