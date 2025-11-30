import crud
from models import Preset
from database import create_db_and_tables

def seed_db():
    create_db_and_tables()
    presets = [
        Preset(name="Get Version", description="Displays the Betaflight firmware version.", tags=["info", "diagnostics"], content="version", author="BFQuickLoad"),
        Preset(name="Dump All Settings", description="Dumps all current Betaflight settings to the CLI.", tags=["backup", "settings"], content="dump", author="BFQuickLoad"),
        Preset(name="Dump Diff", description="Dumps only settings that differ from the default values.", tags=["backup", "settings"], content="diff", author="BFQuickLoad"),
        Preset(name="Save Settings", description="Saves current settings to permanent memory.", tags=["action", "settings"], content="save", author="BFQuickLoad"),
        Preset(name="Load Defaults", description="Loads factory default settings (requires 'save' afterwards).", tags=["action", "settings", "defaults"], content="defaults", author="BFQuickLoad"),
        Preset(name="Show PID Profile", description="Displays the active PID profile settings.", tags=["info", "tuning"], content="get pid_profile", author="BFQuickLoad"),
        Preset(name="Show Filter Settings", description="Displays all filter-related settings.", tags=["info", "filters"], content="get dterm_filter", author="BFQuickLoad"),
        # Presets from Betaflight_Dumps.pdf, extracted by Luki
        Preset(name="Tiny Hoop Aux Mixes", description="Auxiliary and adjustment ranges for Tiny Hoop with Airmode via throttle.", tags=["aux", "mix", "airmode", "tinywhoop"], content="""# aux
aux 0 0 0 1700 2100 0 0
aux 1 1 3 900 1700 0 0
aux 2 13 4 1700 2100 0 0
aux 3 28 7 900 1300 0 0
aux 4 35 2 1700 2100 0 0
aux 5 0 0 900 900 0 0
aux 6 0 0 900 900 0 0
aux 7 0 0 900 900 0 0
aux 8 0 0 900 900 0 0
aux 9 0 0 900 900 0 0
aux 10 0 0 900 900 0 0
aux 11 0 0 900 900 0 0
aux 12 0 0 900 900 0 0
aux 13 0 0 900 900 0 0
aux 14 0 0 900 900 0 0
aux 15 0 0 900 900 0 0
aux 16 0 0 900 900 0 0
aux 17 0 0 900 900 0 0
aux 18 0 0 900 900 0 0
aux 19 0 0 900 900 0 0
# adjrange
adjrange 0 0 3 900 1700 12 10 0 0
adjrange 1 0 3 1700 2100 12 6 0 0
adjrange 2 0 5 900 2100 29 5 0 0
adjrange 3 0 0 900 900 0 0 0 0
adjrange 4 0 0 900 900 0 0 0 0
adjrange 5 0 0 900 900 0 0 0 0
adjrange 6 0 0 900 900 0 0 0 0
adjrange 7 0 0 900 900 0 0 0 0
adjrange 8 0 0 900 900 0 0 0 0
adjrange 9 0 0 900 900 0 0 0 0
adjrange 10 0 0 900 900 0 0 0 0
adjrange 11 0 0 900 900 0 0 0 0
adjrange 12 0 0 900 900 0 0 0 0
adjrange 13 0 0 900 900 0 0 0 0
adjrange 14 0 0 900 900 0 0 0 0
adjrange 15 0 0 900 900 0 0 0 0
adjrange 16 0 0 900 900 0 0 0 0
adjrange 17 0 0 900 900 0 0 0 0
adjrange 18 0 0 900 900 0 0 0 0
adjrange 19 0 0 900 900 0 0 0 0
adjrange 20 0 0 900 900 0 0 0 0
adjrange 21 0 0 900 900 0 0 0 0
adjrange 22 0 0 900 900 0 0 0 0
adjrange 23 0 0 900 900 0 0 0 0
adjrange 24 0 0 900 900 0 0 0 0
adjrange 25 0 0 900 900 0 0 0 0
adjrange 26 0 0 900 900 0 0 0 0
adjrange 27 0 0 900 900 0 0 0 0
adjrange 28 0 0 900 900 0 0 0 0
adjrange 29 0 0 900 900 0 0 0 0""", author="Luki"),
        Preset(name="Longrange Aux with LED Blinker", description="Auxiliary and adjustment ranges for Longrange setup including LED blinker.", tags=["aux", "longrange", "led", "mix"], content="""# aux
aux 0 0 0 1700 2100 0 0
aux 1 1 3 1250 2100 0 0
aux 2 13 4 1700 2100 0 0
aux 3 26 0 1700 2100 0 0
aux 4 35 2 1700 2100 0 0
aux 5 36 1 1700 2100 0 0
aux 6 0 0 900 900 0 0
aux 7 0 0 900 900 0 0
aux 8 0 0 900 900 0 0
aux 9 0 0 900 900 0 0
aux 10 0 0 900 900 0 0
aux 11 0 0 900 900 0 0
aux 12 0 0 900 900 0 0
aux 13 0 0 900 900 0 0
aux 14 0 0 900 900 0 0
aux 15 0 0 900 900 0 0
aux 16 0 0 900 900 0 0
aux 17 0 0 900 900 0 0
aux 18 0 0 900 900 0 0
aux 19 0 0 900 900 0 0
# adjrange
adjrange 0 0 3 1300 2100 12 10 0 0
adjrange 1 0 3 900 1300 12 6 0 0
adjrange 2 0 5 900 2100 29 5 0 0
adjrange 3 0 0 900 900 0 0 0 0
adjrange 4 0 0 900 900 0 0 0 0
adjrange 5 0 0 900 900 0 0 0 0
adjrange 6 0 0 900 900 0 0 0 0
adjrange 7 0 0 900 900 0 0 0 0
adjrange 8 0 0 900 900 0 0 0 0
adjrange 9 0 0 900 900 0 0 0 0
adjrange 10 0 0 900 900 0 0 0 0
adjrange 11 0 0 900 900 0 0 0 0
adjrange 12 0 0 900 900 0 0 0 0
adjrange 13 0 0 900 900 0 0 0 0
adjrange 14 0 0 900 900 0 0 0 0
adjrange 15 0 0 900 900 0 0 0 0
adjrange 16 0 0 900 900 0 0 0 0
adjrange 17 0 0 900 900 0 0 0 0
adjrange 18 0 0 900 900 0 0 0 0
adjrange 19 0 0 900 900 0 0 0 0
adjrange 20 0 0 900 900 0 0 0 0
adjrange 21 0 0 900 900 0 0 0 0
adjrange 22 0 0 900 900 0 0 0 0
adjrange 23 0 0 900 900 0 0 0 0
adjrange 24 0 0 900 900 0 0 0 0
adjrange 25 0 0 900 900 0 0 0 0
adjrange 26 0 0 900 900 0 0 0 0
adjrange 27 0 0 900 900 0 0 0 0
adjrange 28 0 0 900 900 0 0 0 0
adjrange 29 0 0 900 900 0 0 0 0""", author="Luki"),
        Preset(name="OSD Profile Names", description="Sets names for OSD profiles (Min, Fly, Max OSD).", tags=["osd", "display", "profile"], content="""set osd_profile_0_name = Min OSD
set osd_profile_1_name = Fly OSD
set osd_profile_2_name = Max OSD""", author="Luki"),
        Preset(name="DJI OSD Longrange Configuration", description="Comprehensive OSD settings for DJI systems in longrange setups.", tags=["osd", "dji", "longrange", "display"], content="""set osd_units = METRIC
set osd_warn_bitmask = 187391
set osd_cap_alarm = 2200
set osd_alt_alarm = 100
set osd_distance_alarm = 0
set osd_esc_temp_alarm = 0
set osd_esc_rpm_alarm = -1
set osd_esc_current_alarm = -1
set osd_core_temp_alarm = 70
set osd_ah_max_pit = 20
set osd_ah_max_rol = 40
set osd_ah_invert = OFF
set osd_logo_on_arming = OFF
set osd_logo_on_arming_duration = 5
set osd_tim1 = 3
set osd_tim2 = 2561
set osd_vbat_pos = 1544
set osd_rssi_pos = 152
set osd_link_quality_pos = 14922
set osd_link_tx_power_pos = 14784
set osd_rssi_dbm_pos = 6698
set osd_rsnr_pos = 6666
set osd_tim_1_pos = 7721
set osd_tim_2_pos = 608
set osd_remaining_time_estimate_pos = 341
set osd_flymode_pos = 15971
set osd_anti_gravity_pos = 341
set osd_g_force_pos = 4226
set osd_throttle_pos = 14932
set osd_vtx_channel_pos = 373
set osd_crosshairs_pos = 312
set osd_ah_sbar_pos = 313
set osd_ah_pos = 185
set osd_current_pos = 4723
set osd_mah_drawn_pos = 4731
set osd_wh_drawn_pos = 341
set osd_motor_diag_pos = 341
set osd_craft_name_pos = 15977
set osd_pilot_name_pos = 14816
set osd_gps_speed_pos = 14939
set osd_gps_lon_pos = 14368
set osd_gps_lat_pos = 14336
set osd_gps_sats_pos = 15366
set osd_home_dir_pos = 14360
set osd_home_dist_pos = 14361
set osd_flight_dist_pos = 6161
set osd_compass_bar_pos = 54
set osd_altitude_pos = 22559
set osd_pid_roll_pos = 341
set osd_pid_pitch_pos = 341
set osd_pid_yaw_pos = 341
set osd_debug_pos = 341
set osd_power_pos = 4257
set osd_pidrate_profile_pos = 341
set osd_warnings_pos = 14773
set osd_avg_cell_voltage_pos = 15907
set osd_pit_ang_pos = 635
set osd_rol_ang_pos = 341
set osd_battery_usage_pos = 341
set osd_disarmed_pos = 14550
set osd_nheading_pos = 341
set osd_up_down_reference_pos = 312
set osd_ready_mode_pos = 369
set osd_nvario_pos = 341
set osd_esc_tmp_pos = 341
set osd_esc_rpm_pos = 0
set osd_esc_rpm_freq_pos = 341
set osd_rtc_date_time_pos = 341
set osd_adjustment_range_pos = 341
set osd_flip_arrow_pos = 150
set osd_core_temp_pos = 363
set osd_log_status_pos = 4193
set osd_stick_overlay_left_pos = 4352
set osd_stick_overlay_right_pos = 5390
set osd_stick_overlay_radio_mode = 2
set osd_rate_profile_name_pos = 14880
set osd_pid_profile_name_pos = 14912
set osd_profile_name_pos = 14944
set osd_rcchannels_pos = 341
set osd_camera_frame_pos = 110
set osd_efficiency_pos = 341
set osd_total_flights_pos = 341
set osd_aux_pos = 341
set osd_sys_goggle_voltage_pos = 341
set osd_sys_vtx_voltage_pos = 341
set osd_sys_bitrate_pos = 341
set osd_sys_delay_pos = 341
set osd_sys_distance_pos = 341
set osd_sys_lq_pos = 341
set osd_sys_goggle_dvr_pos = 341
set osd_sys_vtx_dvr_pos = 341
set osd_sys_warnings_pos = 341
set osd_sys_vtx_temp_pos = 341
set osd_sys_fan_speed_pos = 341
set osd_stat_bitmask = 1120288474
set osd_profile = 2
set osd_profile_1_name = Fly OSD
set osd_profile_2_name = Max OSD
set osd_profile_3_name = Min OSD
set osd_gps_sats_show_pdop = ON
set osd_displayport_device = MSP
set osd_rcchannels = -1,-1,-1,-1
set osd_camera_frame_width = 24
set osd_camera_frame_height = 11
set osd_stat_avg_cell_value = OFF
set osd_framerate_hz = 12
set osd_menu_background = TRANSPARENT
set osd_aux_channel = 1
set osd_aux_scale = 200
set osd_aux_symbol = 65
set osd_canvas_width = 53
set osd_canvas_height = 20
set osd_craftname_msgs = OFF""", author="Luki"),
        Preset(name="Analog OSD Universal Configuration", description="Universal OSD settings for analog FPV systems.", tags=["osd", "analog", "display"], content="""set osd_units = METRIC
set osd_warn_bitmask = 312191
set osd_rssi_alarm = 20
set osd_cap_alarm = 2200
set osd_alt_alarm = 100
set osd_distance_alarm = 0
set osd_esc_temp_alarm = 0
set osd_esc_rpm_alarm = -1
set osd_esc_current_alarm = -1
set osd_core_temp_alarm = 70
set osd_ah_max_pit = 20
set osd_ah_max_rol = 40
set osd_ah_invert = OFF
set osd_logo_on_arming = OFF
set osd_logo_on_arming_duration = 5
set osd_tim1 = 2560
set osd_tim2 = 2561
set osd_vbat_pos = 6551
set osd_rssi_pos = 226
set osd_link_quality_pos = 6529
set osd_link_tx_power_pos = 341
set osd_rssi_dbm_pos = 4449
set osd_rsnr_pos = 341
set osd_tim_1_pos = 386
set osd_tim_2_pos = 4471
set osd_remaining_time_estimate_pos = 33
set osd_flymode_pos = 4417
set osd_anti_gravity_pos = 341
set osd_g_force_pos = 341
set osd_throttle_pos = 4441
set osd_vtx_channel_pos = 4150
set osd_crosshairs_pos = 6349
set osd_ah_sbar_pos = 313
set osd_ah_pos = 185
set osd_current_pos = 264
set osd_mah_drawn_pos = 386
set osd_wh_drawn_pos = 341
set osd_motor_diag_pos = 341
set osd_craft_name_pos = 6540
set osd_pilot_name_pos = 341
set osd_gps_speed_pos = 341
set osd_gps_lon_pos = 341
set osd_gps_lat_pos = 341
set osd_gps_sats_pos = 341
set osd_home_dir_pos = 341
set osd_home_dist_pos = 98
set osd_flight_dist_pos = 130
set osd_compass_bar_pos = 341
set osd_altitude_pos = 341
set osd_pid_roll_pos = 341
set osd_pid_pitch_pos = 341
set osd_pid_yaw_pos = 341
set osd_debug_pos = 341
set osd_power_pos = 341
set osd_pidrate_profile_pos = 341
set osd_warnings_pos = 14633
set osd_avg_cell_voltage_pos = 44
set osd_pit_ang_pos = 97
set osd_rol_ang_pos = 65
set osd_battery_usage_pos = 341
set osd_disarmed_pos = 6379
set osd_nheading_pos = 341
set osd_up_down_reference_pos = 312
set osd_ready_mode_pos = 341
set osd_nvario_pos = 341
set osd_esc_tmp_pos = 163
set osd_esc_rpm_pos = 150
set osd_esc_rpm_freq_pos = 341
set osd_rtc_date_time_pos = 341
set osd_adjustment_range_pos = 341
set osd_flip_arrow_pos = 341
set osd_core_temp_pos = 278
set osd_log_status_pos = 341
set osd_stick_overlay_left_pos = 341
set osd_stick_overlay_right_pos = 341
set osd_stick_overlay_radio_mode = 2
set osd_rate_profile_name_pos = 4129
set osd_pid_profile_name_pos = 341
set osd_profile_name_pos = 341
set osd_rcchannels_pos = 341
set osd_camera_frame_pos = 142
set osd_efficiency_pos = 341
set osd_total_flights_pos = 341
set osd_aux_pos = 341
set osd_sys_goggle_voltage_pos = 341
set osd_sys_vtx_voltage_pos = 341
set osd_sys_bitrate_pos = 341
set osd_sys_delay_pos = 341
set osd_sys_distance_pos = 341
set osd_sys_lq_pos = 341
set osd_sys_goggle_dvr_pos = 341
set osd_sys_vtx_dvr_pos = 341
set osd_sys_warnings_pos = 341
set osd_sys_vtx_temp_pos = 341
set osd_sys_fan_speed_pos = 341
set osd_stat_bitmask = 8520228
set osd_profile = 2
set osd_profile_1_name = -
set osd_profile_2_name = -
set osd_profile_3_name = -
set osd_gps_sats_show_pdop = OFF
set osd_displayport_device = AUTO
set osd_rcchannels = -1,-1,-1,-1
set osd_camera_frame_width = 24
set osd_camera_frame_height = 11
set osd_stat_avg_cell_value = OFF
set osd_framerate_hz = 12
set osd_menu_background = TRANSPARENT
set osd_aux_channel = 1
set osd_aux_scale = 200
set osd_aux_symbol = 65
set osd_canvas_width = 30
set osd_canvas_height = 13
set osd_craftname_msgs = OFF""", author="Luki"),
        Preset(name="RSSI Warning (5 Inch, Bad RX)", description="OSD RSSI warning settings for 5-inch drones with poor receiver signal.", tags=["rssi", "alarm", "osd", "5inch"], content="""set osd_link_quality_alarm = 75
set osd_rssi_dbm_alarm = -85
set osd_rsnr_alarm = 0""", author="Luki"),
        Preset(name="RSSI Warning (5 Inch, Good RX)", description="OSD RSSI warning settings for 5-inch drones with good receiver signal.", tags=["rssi", "alarm", "osd", "5inch"], content="""set osd_link_quality_alarm = 75
set osd_rssi_dbm_alarm = -99
set osd_rsnr_alarm = 0""", author="Luki"),
        Preset(name="Air65 RSSI Warnings", description="OSD RSSI warning settings for Air65 drones.", tags=["rssi", "alarm", "osd", "air65"], content="""set osd_link_quality_alarm = 75
set osd_rssi_dbm_alarm = -95
set osd_rsnr_alarm = 0""", author="Luki"),
        Preset(name="Air65 PID Tuning", description="PID, iterm, and acro trainer settings for Air65 drones.", tags=["pid", "tuning", "air65"], content="""# profile 0
set profile_name = HQ 31mm
set dterm_lpf1_dyn_min_hz = 75
set dterm_lpf1_dyn_max_hz = 150
set dterm_lpf1_dyn_expo = 5
set dterm_lpf1_type = PT1
set dterm_lpf1_static_hz = 75
set dterm_lpf2_type = PT1
set dterm_lpf2_static_hz = 150
set dterm_notch_hz = 0
set dterm_notch_cutoff = 0
set vbat_sag_compensation = 100
set pid_at_min_throttle = ON
set anti_gravity_gain = 80
set anti_gravity_cutoff_hz = 5
set anti_gravity_p_gain = 100
set acc_limit_yaw = 0
set acc_limit = 0
set crash_dthreshold = 50
set crash_gthreshold = 400
set crash_setpoint_threshold = 350
set crash_time = 500
set crash_delay = 0
set crash_recovery_angle = 10
set crash_recovery_rate = 100
set crash_limit_yaw = 200
set crash_recovery = OFF
set iterm_rotation = OFF
set iterm_relax = RP
set iterm_relax_type = SETPOINT
set iterm_relax_cutoff = 15
set iterm_windup = 85
set iterm_limit = 400
set pidsum_limit = 500
set pidsum_limit_yaw = 400
set yaw_lowpass_hz = 100
set throttle_boost = 5
set throttle_boost_cutoff = 15
set acro_trainer_angle_limit = 20
set acro_trainer_lookahead_ms = 50
set acro_trainer_debug_axis = ROLL
set acro_trainer_gain = 75
set p_pitch = 77
set i_pitch = 138
set d_pitch = 50
set f_pitch = 0
set p_roll = 67
set i_roll = 119
set d_roll = 44
set f_roll = 0
set p_yaw = 67
set i_yaw = 119
set d_yaw = 0
set f_yaw = 0
set angle_p_gain = 100
set angle_feedforward = 50
set angle_feedforward_smoothing_ms = 80
set angle_limit = 45
set angle_earth_ref = 100
set horizon_level_strength = 75
set horizon_limit_sticks = 75
set horizon_limit_degrees = 135
set horizon_ignore_sticks = OFF
set horizon_delay_ms = 500
set abs_control_gain = 0
set abs_control_limit = 90
set abs_control_error_limit = 20
set abs_control_cutoff = 11
set use_integrated_yaw = OFF
set integrated_yaw_relax = 200
set d_min_roll = 44
set d_min_pitch = 50
set d_min_yaw = 0
set d_max_gain = 20
set d_max_advance = 20
set motor_output_limit = 100
set auto_profile_cell_count = 1
set launch_control_mode = NORMAL
set launch_trigger_allow_reset = ON
set launch_trigger_throttle_percent = 20
set launch_angle_limit = 0
set launch_control_gain = 40
set thrust_linear = 20
set transient_throttle_limit = 0
set feedforward_transition = 0
set feedforward_averaging = 2_POINT
set feedforward_smooth_factor = 35
set feedforward_jitter_factor = 4
set feedforward_boost = 18
set feedforward_max_rate_limit = 90
set dyn_idle_min_rpm = 0
set dyn_idle_p_gain = 50
set dyn_idle_i_gain = 50
set dyn_idle_d_gain = 50
set dyn_idle_max_increase = 150
set dyn_idle_start_increase = 50
set level_race_mode = OFF
set simplified_pids_mode = RPY
set simplified_master_multiplier = 130
set simplified_i_gain = 100
set simplified_d_gain = 115
set simplified_pi_gain = 115
set simplified_dmax_gain = 0
set simplified_feedforward_gain = 0
set simplified_pitch_d_gain = 100
set simplified_pitch_pi_gain = 110
set simplified_dterm_filter = ON
set simplified_dterm_filter_multiplier = 100
set tpa_mode = PD
set tpa_rate = 55
set tpa_breakpoint = 1350
set tpa_low_rate = 20
set tpa_low_breakpoint = 1050
set tpa_low_always = OFF
set ez_landing_threshold = 25
set ez_landing_limit = 15
set ez_landing_speed = 50""", author="Luki"),
        Preset(name="GPS Qualifier", description="OSD setting for displaying GPS satellite PDOP.", tags=["gps", "osd", "diagnostics"], content="""set osd_gps_sats_show_pdop = ON""", author="Luki"),
        Preset(name="5 Inch Rates - R Flink (Profile 0)", description="Rate profile 0 for 5-inch drones: R Flink style.", tags=["rates", "5inch", "rflink", "profile0"], content="""# rateprofile 0
set rateprofile_name = R Flink
set thr_mid = 50
set thr_expo = 0
set rates_type = ACTUAL
set quickrates_rc_expo = OFF
set roll_rc_rate = 20
set pitch_rc_rate = 20
set yaw_rc_rate = 15
set roll_expo = 45
set pitch_expo = 35
set yaw_expo = 30
set roll_srate = 100
set pitch_srate = 100
set yaw_srate = 82
set throttle_limit_type = OFF
set throttle_limit_percent = 100
set roll_rate_limit = 1998
set pitch_rate_limit = 1998
set yaw_rate_limit = 1998""", author="Luki"),
        Preset(name="5 Inch Rates - R Mix (Profile 1)", description="Rate profile 1 for 5-inch drones: R Mix style.", tags=["rates", "5inch", "rmix", "profile1"], content="""# rateprofile 1
set rateprofile_name = R Mix
set thr_mid = 41
set thr_expo = 0
set rates_type = ACTUAL
set quickrates_rc_expo = OFF
set roll_rc_rate = 22
set pitch_rc_rate = 22
set yaw_rc_rate = 22
set roll_expo = 100
set pitch_expo = 100
set yaw_expo = 100
set roll_srate = 100
set pitch_srate = 100
set yaw_srate = 82
set throttle_limit_type = OFF
set throttle_limit_percent = 100
set roll_rate_limit = 1998
set pitch_rate_limit = 1998
set yaw_rate_limit = 1998
set roll_level_expo = 0
set pitch_level_expo = 0""", author="Luki"),
        Preset(name="5 Inch Rates - R Angle (Profile 2)", description="Rate profile 2 for 5-inch drones: R Angle style.", tags=["rates", "5inch", "rangle", "profile2"], content="""# rateprofile 2
set rateprofile_name = R Angle
set thr_mid = 46
set thr_expo = 0
set rates_type = ACTUAL
set quickrates_rc_expo = OFF
set roll_rc_rate = 15
set pitch_rc_rate = 15
set yaw_rc_rate = 10
set roll_expo = 100
set pitch_expo = 100
set yaw_expo = 100
set roll_srate = 50
set pitch_srate = 50
set yaw_srate = 82
set throttle_limit_type = OFF
set throttle_limit_percent = 100
set roll_rate_limit = 1998
set pitch_rate_limit = 1998
set yaw_rate_limit = 1998""", author="Luki"),
        Preset(name="5 Inch Rates - R Exakt (Profile 1 - Alt)", description="Alternative rate profile 1 for 5-inch drones: R Exakt style.", tags=["rates", "5inch", "rexakt", "profile1"], content="""# rateprofile 1
set rateprofile_name = R Exakt
set thr_mid = 50
set thr_expo = 0
set rates_type = ACTUAL
set quickrates_rc_expo = OFF
set roll_rc_rate = 9
set pitch_rc_rate = 9
set yaw_rc_rate = 10
set roll_expo = 50
set pitch_expo = 45
set yaw_expo = 40
set roll_srate = 100
set pitch_srate = 100
set yaw_srate = 82
set throttle_limit_type = OFF
set throttle_limit_percent = 100
set roll_rate_limit = 1998
set pitch_rate_limit = 1998
set yaw_rate_limit = 1998""", author="Luki"),
        Preset(name="5 Inch Rates - R Angle (Profile 2 - Alt)", description="Alternative rate profile 2 for 5-inch drones: R Angle style.", tags=["rates", "5inch", "rangle", "profile2"], content="""# rateprofile 2
set rateprofile_name = R Angle
set thr_mid = 46
set thr_expo = 0
set rates_type = ACTUAL
set quickrates_rc_expo = OFF
set roll_rc_rate = 15
set pitch_rc_rate = 15
set yaw_rc_rate = 10
set roll_expo = 100
set pitch_expo = 100
set yaw_expo = 100
set roll_srate = 50
set pitch_srate = 50
set yaw_srate = 82
set throttle_limit_type = OFF
set throttle_limit_percent = 100
set roll_rate_limit = 1998
set pitch_rate_limit = 1998
set yaw_rate_limit = 1998""", author="Luki"),
        Preset(name="5 Inch Rates - R Exakt (Profile 3)", description="Rate profile 3 for 5-inch drones: R Exakt style.", tags=["rates", "5inch", "rexakt", "profile3"], content="""# rateprofile 3
set rateprofile_name = R Exakt
set thr_mid = 50
set thr_expo = 0
set rates_type = ACTUAL
set quickrates_rc_expo = OFF
set roll_rc_rate = 9
set pitch_rc_rate = 9
set yaw_rc_rate = 15
set roll_expo = 45
set pitch_expo = 35
set yaw_expo = 30
set roll_srate = 100
set pitch_srate = 100
set yaw_srate = 82
set throttle_limit_type = OFF
set throttle_limit_percent = 100
set roll_rate_limit = 1998
set pitch_rate_limit = 1998
set yaw_rate_limit = 1998""", author="Luki"),
        Preset(name="Legacy Rates - R Expo (Profile 0)", description="Legacy rate profile 0 for R Expo style.", tags=["rates", "legacy", "rexpo", "profile0"], content="""# rateprofile 0
set rateprofile_name = R Expo
set thr_mid = 30
set thr_expo = 0
set rates_type = ACTUAL
set quickrates_rc_expo = OFF
set roll_rc_rate = 7
set pitch_rc_rate = 7
set yaw_rc_rate = 10
set roll_expo = 35
set pitch_expo = 35
set yaw_expo = 25
set roll_srate = 100
set pitch_srate = 100
set yaw_srate = 82
set throttle_limit_type = OFF
set throttle_limit_percent = 100
set roll_rate_limit = 1998
set pitch_rate_limit = 1998
set yaw_rate_limit = 1998""", author="Luki"),
        Preset(name="Tinywhoop Rates - R Race (Profile 0)", description="Rate profile 0 for Tinywhoop drones: R Race style.", tags=["rates", "tinywhoop", "rrace", "profile0"], content="""# rateprofile 0
set rateprofile_name = R Race
set rates_type = ACTUAL
set quickrates_rc_expo = OFF
set roll_rc_rate = 14
set pitch_rc_rate = 14
set yaw_rc_rate = 14
set roll_expo = 50
set pitch_expo = 50
set yaw_expo = 50
set roll_srate = 53
set pitch_srate = 53
set yaw_srate = 53
set throttle_limit_type = OFF
set throttle_limit_percent = 100
set roll_rate_limit = 1998
set pitch_rate_limit = 1998""", author="Luki"),
        Preset(name="Tinywhoop Rates - R Mix (Profile 1)", description="Rate profile 1 for Tinywhoop drones: R Mix style.", tags=["rates", "tinywhoop", "rmix", "profile1"], content="""# rateprofile 1
set rateprofile_name = R Mix
set rates_type = ACTUAL
set quickrates_rc_expo = OFF
set roll_rc_rate = 22
set pitch_rc_rate = 22
set yaw_rc_rate = 22
set roll_expo = 100
set pitch_expo = 100
set yaw_expo = 100
set roll_srate = 100
set pitch_srate = 100
set yaw_srate = 82
set throttle_limit_type = OFF
set throttle_limit_percent = 100
set roll_rate_limit = 1998
set pitch_rate_limit = 1998
set yaw_rate_limit = 1998
set roll_level_expo = 0
set pitch_level_expo = 0""", author="Luki"),
        Preset(name="Tinywhoop Rates - R Angle (Profile 2)", description="Rate profile 2 for Tinywhoop drones: R Angle style.", tags=["rates", "tinywhoop", "rangle", "profile2"], content="""# rateprofile 2
set rateprofile_name = R Angle
set rates_type = ACTUAL
set quickrates_rc_expo = OFF
set roll_rc_rate = 40
set pitch_rc_rate = 40
set yaw_rc_rate = 22
set roll_expo = 100
set pitch_expo = 100
set yaw_expo = 100
set roll_srate = 100
set pitch_srate = 100
set yaw_srate = 82
set throttle_limit_type = OFF
set throttle_limit_percent = 100
set roll_rate_limit = 1998
set pitch_rate_limit = 1998
set yaw_rate_limit = 1998
set roll_level_expo = 0
set pitch_level_expo = 0""", author="Luki"),
        Preset(name="Tinywhoop Throttle Expo (30.000kv)", description="Throttle expo settings for 30.000kv Tinywhoop motors across three rate profiles.", tags=["throttle", "expo", "tinywhoop", "30000kv"], content="""# rateprofile 0
set thr_mid = 31
set thr_expo = 20
# rateprofile 1
set thr_mid = 31
set thr_expo = 20
# rateprofile 2
set thr_mid = 31
set thr_expo = 50""", author="Luki"),
        Preset(name="Tinywhoop Throttle Expo (27.000kv)", description="Throttle expo settings for 27.000kv Tinywhoop motors across three rate profiles.", tags=["throttle", "expo", "tinywhoop", "27000kv"], content="""# rateprofile 0
set thr_mid = 35
set thr_expo = 20
# rateprofile 1
set thr_mid = 35
set thr_expo = 20
# rateprofile 2
set thr_mid = 35
set thr_expo = 50""", author="Luki"),
        Preset(name="Tinywhoop Throttle Expo (23.000kv)", description="Throttle expo settings for 23.000kv Tinywhoop motors across three rate profiles.", tags=["throttle", "expo", "tinywhoop", "23000kv"], content="""# rateprofile 0
set thr_mid = 41
set thr_expo = 20
# rateprofile 1
set thr_mid = 41
set thr_expo = 20
# rateprofile 2
set thr_mid = 41
set thr_expo = 50""", author="Luki"),
    ]
    for preset in presets:
        crud.create_preset(preset)
    print("Database seeded with dummy data.")

if __name__ == "__main__":
    seed_db()
