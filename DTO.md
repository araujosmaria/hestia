<!DOCTYPE html>
<!-- saved from url=(0061)https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-a11y-link-underlines="true" data-css-features="one_click_merge_conflict" data-turbo-loaded=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style><style>
:root {
  --fontStack-monospace: "Monaspace Neon", ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace !important;
}
</style>




  
    
  
  
  
  
  
  

  

  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/light-6215e264aa81.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/dark-be3560533a2e.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-0d1726fbc5ce.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-295e85c7acf3.css"><link data-color-theme="light_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind_high_contrast-6f7fd702e376.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-5810b6198753.css"><link data-color-theme="light_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia_high_contrast-9be09d7c543a.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-0f500fc95568.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-b93c131e97d5.css"><link data-color-theme="dark_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind_high_contrast-562d56be7ab1.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-297cb06a83c5.css"><link data-color-theme="dark_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia_high_contrast-9ba270e719b9.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-64c3ca7e9c26.css"><link data-color-theme="dark_dimmed_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed_high_contrast-89581edef127.css">

  <style type="text/css">
    :root {
      --tab-size-preference: 4;
    }

    pre, code {
      tab-size: var(--tab-size-preference);
    }
  </style>

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/primer-primitives-15839d47b75d.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/primer-f96b923db733.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/global-48a457f3b81b.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/github-73fd10e24e0c.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/repository-5d735668c600.css">

  

  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["alternate_user_config_repo","api_insights_show_missing_data_banner","attestations_filtering","attestations_sorting","billing_fixed_amount_metered_configured_discounts","billing_hard_budget_limits_for_licenses","billing_use_current_discounts_list_dialog_v2","client_version_header","codespaces_prebuild_region_target_update","contact_sales_locale_utm_medium","contentful_lp_enterprise","contentful_lp_footnotes","copilot_agent_cli_public_preview","copilot_agent_tasks_btn_code_nav","copilot_agent_tasks_btn_code_view","copilot_agent_tasks_btn_code_view_lines","copilot_agent_tasks_btn_file_reference","copilot_api_agentic_issue_marshal_yaml","copilot_api_draft_issue_code_search","copilot_api_github_draft_update_issue_skill","copilot_bing_search_use_azure_ai_agent_service","copilot_bing_search_use_grounding_ui","copilot_chat_attach_multiple_images","copilot_chat_disable_model_picker_while_streaming","copilot_chat_file_redirect","copilot_chat_multi_file_picker_attachment","copilot_chat_opening_thread_switch","copilot_chat_reduce_quota_checks","copilot_chat_search_bar_redirect","copilot_chat_selection_attachments","copilot_chat_vision_in_claude","copilot_chat_vision_skip_thread_create","copilot_coding_agent_diff_stats","copilot_coding_agent_ga","copilot_custom_copilots","copilot_custom_copilots_feature_preview","copilot_duplicate_thread","copilot_extensions_deprecation_notice","copilot_features_raycast_logo","copilot_file_block_ref_matching","copilot_free_to_paid_telem","copilot_ftp_hyperspace_upgrade_prompt","copilot_ftp_settings_upgrade","copilot_ftp_upgrade_to_pro_from_models","copilot_ftp_your_copilot_settings","copilot_generate_commit_message_blob_public_preview","copilot_generate_commit_message_regenerate","copilot_global_overlay_v2","copilot_immersive_agent_branch_selection","copilot_immersive_planning_agent_aggregate_task","copilot_immersive_structured_model_picker","copilot_issue_list_show_more","copilot_no_floating_button","copilot_pipes_github_graphql_nodes","copilot_premium_request_quotas","copilot_read_shared_conversation","copilot_share_active_subthread","copilot_show_copilot_sub_issues_button_on_issues_page","copilot_spaces_as_attachments","copilot_spaces_ga","copilot_spark_allow_empty_commit","copilot_spark_loading_webgl","copilot_spark_progressive_error_handling","copilot_spark_read_iteration_history_from_git_v2","copilot_spark_single_user_iteration","copilot_spark_use_billing_headers","copilot_spark_write_iteration_history_to_git","copilot_stable_conversation_view","copilot_workbench_agent_seed_tool","copilot_workbench_cache","copilot_workbench_connection_reload_banner","copilot_workbench_preview_analytics","copilot_workbench_ratelimit_fallback","copilot_workbench_refresh_on_wsod","copilot_workbench_synthetic_generation","dashboard_public_preview","direct_to_salesforce","dotcom_chat_client_side_skills","failbot_report_error_react_apps_on_page","fgpat_permissions_selector_redesign","ghost_pilot_confidence_truncation_25","ghost_pilot_confidence_truncation_40","global_nav_copilot_a11y_fix","global_search_multi_orgs","global_sso_banner","hpc_improve_dom_insertion_observer","inp_reduced_threshold","insert_before_patch","issue_fields_report_usage","issues_copilot_cross_repo_assign","issues_copilot_repo_search_in_org","issues_expanded_file_types","issues_react_blur_item_picker_on_close","issues_react_bots_timeline_pagination","issues_react_include_bots_in_pickers","issues_react_prohibit_title_fallback","issues_react_remove_placeholders","issues_sticky_sidebar","kb_semantic_api_migration","lifecycle_label_name_updates","link_contact_sales_swp_marketo","marketing_pages_search_explore_provider","marketplace_async_recently_added","mcp_registry_install","memex_mwl_filter_field_delimiter","memex_roadmap_drag_style","migrate_toasts_to_banners_web_notifications","new_traffic_page_banner","one_click_merge_conflict","override_pulse_legacy_url","pinned_issue_fields","primer_react_segmented_control_tooltip","primer_react_unified_portal_root","pru_billing_page","record_sso_banner_metrics","releases_update_ref_selector","remove_child_patch","repos_insights_remove_new_url","repository_suggester_elastic_search","sample_network_conn_type","scheduled_reminders_updated_limits","site_homepage_collaborate_video","site_homepage_contentful","site_msbuild_webgl_hero","spark_commit_on_default_branch","spark_show_data_access_on_publish","spark_sync_repository_after_iteration","viewscreen_sandbox","webp_support","workbench_default_sonnet4","workbench_store_readonly"],"login":"FernandaBighi","copilotApiOverrideUrl":"https://api.individual.githubcopilot.com"}</script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/wp-runtime-1968a65dc189.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_oddbird_popover-polyfill_dist_popover-fn_js-468bf7cab607.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-2f4e04-280c10ec004d.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_arianotify-polyfill_ariaNotify-polyfill_js-node_modules_github_mi-c8eeba-690858154b11.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/environment-e36acb721009.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_primer_behaviors_dist_esm_index_mjs-7e8c9c5d642d.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_selector-observer_dist_index_esm_js-7e4d99c9171d.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_relative-time-element_dist_index_js-c98257dc79a7.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_auto-complete-element_dist_index_js-node_modules_github_catalyst_-0d7d60-55f9488be32e.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_text-expander-element_dist_index_js-754f5b5e9e7e.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-665e70-a5590c456d33.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_markdown-toolbar-element_dist_index_js-d41270eb61be.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-777ce2-337f60509a95.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/github-elements-36a69695b2e8.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/element-registry-e4593824c04e.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_braintree_browser-detection_dist_browser-detection_js-node_modules_githu-bb80ec-4e90f1d1076c.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_lit-html_lit-html_js-06c8637a6071.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_morphdom_dist_morphdom-e-c1896e-8b29325c0a25.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-8eb9b2209bcd.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-893f9f-cd5d89ebdb50.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_hotkey_dist_index_js-node_modules_github_hydro-analytics-client_d-dd3ec8-82973d2f342e.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_quote-selection_dist_index_js-node_modules_github_session-resume_-31b9f3-99d95b37aa24.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_document-metadata_document-metadata_ts-packages_failbot_failbot_ts-b8e9eefcce78.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_updatable-content_updatable-content_ts-a743e72edcf2.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_details-6493f1-b7112815a1fc.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_throttled-input_ts-047775-f7905105dea8.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-6bc7a8849328.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/behaviors-61b516b0ac00.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-ef6d0f-90a0269c4bc0.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/notifications-global-f5c28dea1388.js.baixados" defer="defer"></script>
  
  <script crossorigin="anonymous" type="application/javascript" src="./DTO_files/primer-react-477997561c04.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/react-core-f6571bc10d64.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/react-lib-17ccbc80f53b.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/octicons-react-0f0d82031c98.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_emotion_is-prop-valid_dist_emotion-is-prop-valid_esm_js-node_modules_emo-1fff13-a67dacb6db80.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_tanstack_query-core_build_modern_mutation_js-node_modules_tanstack_query-9bf7e4-a1bacdef8ef2.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_hydro-analytics-c-c228f9-aac9e0b76853.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_swc_helpers_esm__class_private_method_get_js-node_modules_swc_helpers_es-d6b1a6-86b1b1957ff2.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_primer_styled-react_dist_index_js-node_modules_swc_helpers_esm__define_p-af893a-aa5fc5be335a.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_notifications-subscriptions-menu_entry_ts-packages_promise-with-resolvers-polyfill_p-df0233-37157a955eee.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/notifications-subscriptions-menu-d88d4cd8eac4.js.baixados" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/primer-react.2ceb2571848317ce36f7.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/notifications-subscriptions-menu.44a4ce5e60cfd5c27b1a.module.css">


  



  
  
  
  

    
  


  


    


  
  

  
  

    



  

  




    

  

    

    

      

      

    
    
    

      
  
  


      
      


      


      
      
      

        


  <meta http-equiv="x-pjax-version" content="8a232c01b16a155cc3c89505345f728dea2744841e3f4cfa9e419d6c4ffb6bea" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="c922ef32c4ab94f8b870c62883f3e41755ec705db76ec4efb0d343458f1e28c7" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="e41f5e9938c1f58f3f3a63eefa43c32feab3ad64f1c0ef4a9e1a60685fa11e6e" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="8e941aeab3a30addd3761548272a1c1ca682c7b858fd7c322a1353760f9dfc5a" data-turbo-track="reload">

  

      

  



    

    


  

  

  
  

  
  
  




  
  

  

  <link rel="stylesheet" type="text/css" href="./DTO_files/lazy-react-partial-keyboard-shortcuts-dialog.2de9c7d6456a311fce49.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./DTO_files/lazy-react-partial-global-copilot-menu.e8b96f8e81aaf397c759.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./DTO_files/lazy-react-partial-global-create-menu.4d24ecb322134c573644.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./DTO_files/lazy-react-partial-global-user-nav-drawer.c2bc1ffb732493d0bf54.module.css" crossorigin="anonymous"><style id="ms-consent-banner-main-styles">.w8hcgFksdo30C8w-bygqu{color:#000}.ydkKdaztSS0AeHWIeIHsQ a{color:#0067B8}.erL690_8JwUW-R4bJRcfl{background-color:#EBEBEB;border:none;color:#000}.erL690_8JwUW-R4bJRcfl:enabled:hover{color:#000;background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}.erL690_8JwUW-R4bJRcfl:enabled:focus{background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}.erL690_8JwUW-R4bJRcfl:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2);border:none}._1zNQOqxpBFSokeCLGi_hGr{border:none;background-color:#0067B8;color:#fff}._1zNQOqxpBFSokeCLGi_hGr:enabled:hover{color:#fff;background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}._1zNQOqxpBFSokeCLGi_hGr:enabled:focus{background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}._1zNQOqxpBFSokeCLGi_hGr:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,120,215,0.2);border:none}._23tra1HsiiP6cT-Cka-ycB{position:relative;display:flex;z-index:9999;width:100%;background-color:#F2F2F2;justify-content:space-between;text-align:left}div[dir="rtl"]._23tra1HsiiP6cT-Cka-ycB{text-align:right}._1Upc2NjY8AlDn177YoVj0y{margin:0;padding-left:5%;padding-top:8px;padding-bottom:8px}div[dir="rtl"] ._1Upc2NjY8AlDn177YoVj0y{margin:0;padding:8px 5% 8px 0;float:none}._23tra1HsiiP6cT-Cka-ycB svg{fill:none;max-width:none;max-height:none}._1V_hlU-7jdtPiooHMu89BB{display:table-cell;padding:12px;width:24px;height:24px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:24px;line-height:0}.f6QKJD7fhSbnJLarTL-W-{display:table-cell;vertical-align:middle;padding:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:16px}.f6QKJD7fhSbnJLarTL-W- a{text-decoration:underline}._2j0fmugLb1FgYz6KPuB91w{display:inline-block;margin-left:5%;margin-right:5%;min-width:40%;min-width:calc((150px + 3 * 4px) * 2 + 150px);min-width:-webkit-fit-content;min-width:-moz-fit-content;min-width:fit-content;align-self:center;position:relative}._1XuCi2WhiqeWRUVp3pnFG3{margin:4px;padding:5px;min-width:150px;min-height:36px;vertical-align:top;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._1XuCi2WhiqeWRUVp3pnFG3:focus{box-sizing:border-box}._1XuCi2WhiqeWRUVp3pnFG3:disabled{cursor:not-allowed}._2bvsb3ubApyZ0UGoQA9O9T{display:block;position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.6);overflow:auto;text-align:left}div[dir="rtl"]._2bvsb3ubApyZ0UGoQA9O9T{text-align:right}div[dir="rtl"] ._2bvsb3ubApyZ0UGoQA9O9T{left:auto;right:0}.AFsJE948muYyzCMktdzuk{position:relative;top:8%;margin-bottom:40px;margin-left:auto;margin-right:auto;box-sizing:border-box;width:640px;background-color:#fff;border:1px solid #0067B8}._3kWyBRbW_dgnMiEyx06Fu4{float:right;z-index:1;margin:2px;padding:12px;border:none;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:13px;display:flex;align-items:center;text-align:center;color:#666;background-color:#fff}div[dir="rtl"] ._3kWyBRbW_dgnMiEyx06Fu4{margin:2px;padding:12px;float:left}.uCYvKvHXrhjNgflv1VqdD{position:static;margin-top:36px;margin-left:36px;margin-right:36px}._17pX1m9O_W--iZbDt3Ta5r{margin-top:0;margin-bottom:12px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:24px;text-transform:none}._1kBkHQ1V1wu3kl-YcLgUr6{height:446px;overflow:auto}._20_nXDf6uFs9Q6wxRXG-I-{margin-top:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._20_nXDf6uFs9Q6wxRXG-I- a{text-decoration:underline}dl._2a0NH_GDQEQe5Ynfo7suVH{margin-top:36px;margin-bottom:0;padding:0;list-style:none;text-transform:none}dt._3j_LCPv7fyXv3A8FIXVwZ4{margin-top:20px;float:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;list-style:none}.k-vxTGFbdq1aOZB2HHpjh{margin:0;padding:0;border:none}._2Bucyy75c_ogoU1g-liB5R{margin:0;padding:0;border-bottom:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;text-transform:none}._63gwfzV8dclrsl2cfd90r{display:inline-block;margin-top:0;margin-bottom:13px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._1l8wM_4mRYGz3Iu7l3BZR7{display:block}._2UE03QS02aZGkslegN_F-i{display:inline-block;position:relative;left:5px;margin-bottom:13px;margin-right:34px;padding:3px}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{margin:0 0 13px 34px;padding:3px;float:none}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{left:auto;right:5px}._23tra1HsiiP6cT-Cka-ycB *::before,._2bvsb3ubApyZ0UGoQA9O9T *::before,._23tra1HsiiP6cT-Cka-ycB *::after,._2bvsb3ubApyZ0UGoQA9O9T *::after{box-sizing:inherit}._1HSFn0HzGo6w4ADApV8-c4{outline:2px solid rgba(0,0,0,0.8)}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2{display:inline-block;position:relative;margin-top:0;margin-left:0;margin-right:0;height:0;width:0;border-radius:0;cursor:pointer;outline:none;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{display:block;position:absolute;top:5px;left:3px;height:19px;width:19px;content:"";border-radius:50%;border:1px solid #000;background-color:#fff}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{left:auto;right:3px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:rgba(0,0,0,0.8)}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label{cursor:not-allowed}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label::before{border:1px solid rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2)}._3RJzeL3l9Rl_lAQEm6VwdX{display:block;position:static;float:right;margin-top:0;margin-bottom:0;margin-left:19px;margin-right:0;padding-top:0;padding-bottom:0;padding-left:8px;padding-right:0;width:80%;width:calc(100% - 19px);font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-transform:none;cursor:pointer;box-sizing:border-box}div[dir="rtl"] ._3RJzeL3l9Rl_lAQEm6VwdX{margin:0 19px 0 0;padding:0 8px 0 0;float:left}.nohp3sIG12ZBhzcMnPala{margin-top:20px;margin-bottom:48px}._2uhaEsmeotZ3P-M0AXo2kF{padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._2uhaEsmeotZ3P-M0AXo2kF:focus{box-sizing:border-box}._2uhaEsmeotZ3P-M0AXo2kF:disabled{cursor:not-allowed}._3tOu1FJ59c_xz_PmI1lKV5{float:right;padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._3tOu1FJ59c_xz_PmI1lKV5:focus{box-sizing:border-box}._3tOu1FJ59c_xz_PmI1lKV5:disabled{cursor:not-allowed}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0;padding:0;float:left}@media only screen and (max-width: 768px){._2j0fmugLb1FgYz6KPuB91w,._1Upc2NjY8AlDn177YoVj0y{padding-top:8px;padding-bottom:12px;padding-left:3.75%;padding-right:3.75%;margin:0;width:92.5%}._23tra1HsiiP6cT-Cka-ycB{display:block}._1XuCi2WhiqeWRUVp3pnFG3{margin-bottom:8px;margin-left:0;margin-right:0;width:100%}._2bvsb3ubApyZ0UGoQA9O9T{overflow:hidden}.AFsJE948muYyzCMktdzuk{top:1.8%;width:93.33%;height:96.4%;overflow:hidden}.uCYvKvHXrhjNgflv1VqdD{margin-top:24px;margin-left:24px;margin-right:24px;height:100%}._1kBkHQ1V1wu3kl-YcLgUr6{height:62%;height:calc(100% - 188px);min-height:50%}._2uhaEsmeotZ3P-M0AXo2kF{width:100%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:12px;margin-left:0;width:100%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 12px 0;padding:0;float:none}}@media only screen and (max-width: 768px) and (orientation: landscape), only screen and (max-height: 260px), only screen and (max-width: 340px){.AFsJE948muYyzCMktdzuk{overflow:auto}}@media only screen and (max-height: 260px), only screen and (max-width: 340px){._1XuCi2WhiqeWRUVp3pnFG3{min-width:0}._3kWyBRbW_dgnMiEyx06Fu4{padding:3%}.uCYvKvHXrhjNgflv1VqdD{margin-top:3%;margin-left:3%;margin-right:3%}._17pX1m9O_W--iZbDt3Ta5r{margin-bottom:3%}._1kBkHQ1V1wu3kl-YcLgUr6{height:calc(79% - 64px)}.nohp3sIG12ZBhzcMnPala{margin-top:5%;margin-bottom:10%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:3%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 3% 0;padding:0;float:none}}
</style><style type="text/css" id="ms-consent-banner-theme-styles">._23tra1HsiiP6cT-Cka-ycB {
            background-color: #24292f !important;
        }.w8hcgFksdo30C8w-bygqu {
            color: #ffffff !important;
        }.ydkKdaztSS0AeHWIeIHsQ a {
            color: #d8b9ff !important;
        }._2bvsb3ubApyZ0UGoQA9O9T {
            background-color: rgba(23, 23, 23, 0.8) !important;
        }.AFsJE948muYyzCMktdzuk {
            background-color: #24292f !important;
            border: 1px solid #d8b9ff !important;
        }._3kWyBRbW_dgnMiEyx06Fu4 {
            color: #d8b9ff !important;
            background-color: #24292f !important;
        }._1zNQOqxpBFSokeCLGi_hGr {
            border: 1px solid #ffffff !important;
            background-color: #ffffff !important;
            color: #1f2328 !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:hover {
            color: #1f2328 !important;
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 1px solid transparent !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:focus {
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 2px solid #ffffff !important;
        }._1zNQOqxpBFSokeCLGi_hGr:disabled {
            opacity: 0.5 !important;
            color: #1f2328 !important;
            background-color: #ffffff !important;
            border: 1px solid transparent !important;
        }.erL690_8JwUW-R4bJRcfl {
            border: 1px solid #eaeef2 !important;
            background-color: #32383f !important;
            color: #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:hover {
            color: #ffffff !important;
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 1px solid #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:focus {
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 2px solid #6e7781 !important;
        }.erL690_8JwUW-R4bJRcfl:disabled {
            opacity: 0.5 !important;
            color: #ffffff !important;
            background-color: #424a53 !important;
            border: 1px solid #6e7781 !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label::before {
            border: 1px solid #d8b9ff !important;
            background-color: #24292f !important;
        }._1HSFn0HzGo6w4ADApV8-c4 {
            outline: 2px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked + label::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::after {
            background-color: #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled + label::before {
            border: 1px solid rgba(227, 227, 227, 0.2) !important;
            background-color: rgba(227, 227, 227, 0.2) !important;
        }</style><link rel="stylesheet" type="text/css" href="./DTO_files/lazy-react-partial-notifications-subscriptions-menu.44a4ce5e60cfd5c27b1a.module.css" crossorigin="anonymous"><style data-styled="active" data-styled-version="5.3.11"></style><link rel="stylesheet" type="text/css" href="./DTO_files/lazy-react-partial-copilot-chat.b9c6ea91ee9df8f32d5e.module.css" crossorigin="anonymous"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/code-9c9b8dc61e74.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/copilot-coding-agent-status.18a276928d4b7c45824e.module.css"><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_virtualized-list_es_index_js-node_modules_github_template-parts_lib_inde-f69fd1-1b826bcef4eb.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-970f7d-4ff5f460b297.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/app_assets_modules_github_ref-selector_ts-98da180bcdc4.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/codespaces-9b7eb41803e5.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-3eebbd-2a60e340f3f8.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_delegated-events_di-e161aa-34194327b80d.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_remote--abdaf7-e83eee3cdca9.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/repositories-08e4f78d2973.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_catalyst_lib_inde-96937f-32b1c20dc237.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/code-menu-f0fbee92a5e1.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_tanstack_query-core_build_modern_queryObserver_js-node_modules_tanstack_-defd52-362960c8d059.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_hydro-analytics-client_dist_analytics-client_js-node_modules_gith-320808-1c166cd40521.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_paths_index_ts-a7343c7f8033.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_agent-sessions_utils_elapsed-time-util_ts-packages_agent-sessions_contexts_PullConte-004f94-a4d6ef1892ab.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_copilot-coding-agent-status_entry_ts-packages_fetch-headers_fetch-headers_ts-package-442e79-2bb344b9ef94.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/copilot-coding-agent-status-57bf0b121fe7.js.baixados" defer="defer"></script><style type="text/css" id="ms-consent-banner-theme-styles"></style><link rel="stylesheet" type="text/css" href="./DTO_files/lazy-react-partial-repos-overview.7ea6d670be60f1a7cf5c.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./DTO_files/packages_code-view-shared_components_files-search_FileResultsList_tsx.b19b01413b9b7d1dd458.module.css" crossorigin="anonymous"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/react-code-view.8b7d2260c74f2a9b531c.module.css"><script type="application/json" id="client-env">{"locale":"en","featureFlags":["alternate_user_config_repo","api_insights_show_missing_data_banner","attestations_filtering","attestations_sorting","billing_fixed_amount_metered_configured_discounts","billing_hard_budget_limits_for_licenses","billing_use_current_discounts_list_dialog_v2","client_version_header","codespaces_prebuild_region_target_update","contact_sales_locale_utm_medium","contentful_lp_enterprise","contentful_lp_footnotes","copilot_agent_cli_public_preview","copilot_agent_tasks_btn_code_nav","copilot_agent_tasks_btn_code_view","copilot_agent_tasks_btn_code_view_lines","copilot_agent_tasks_btn_file_reference","copilot_api_agentic_issue_marshal_yaml","copilot_api_draft_issue_code_search","copilot_api_github_draft_update_issue_skill","copilot_bing_search_use_azure_ai_agent_service","copilot_bing_search_use_grounding_ui","copilot_chat_attach_multiple_images","copilot_chat_disable_model_picker_while_streaming","copilot_chat_file_redirect","copilot_chat_multi_file_picker_attachment","copilot_chat_opening_thread_switch","copilot_chat_reduce_quota_checks","copilot_chat_search_bar_redirect","copilot_chat_selection_attachments","copilot_chat_vision_in_claude","copilot_chat_vision_skip_thread_create","copilot_coding_agent_diff_stats","copilot_coding_agent_ga","copilot_custom_copilots","copilot_custom_copilots_feature_preview","copilot_duplicate_thread","copilot_extensions_deprecation_notice","copilot_features_raycast_logo","copilot_file_block_ref_matching","copilot_free_to_paid_telem","copilot_ftp_hyperspace_upgrade_prompt","copilot_ftp_settings_upgrade","copilot_ftp_upgrade_to_pro_from_models","copilot_ftp_your_copilot_settings","copilot_generate_commit_message_blob_public_preview","copilot_generate_commit_message_regenerate","copilot_global_overlay_v2","copilot_immersive_agent_branch_selection","copilot_immersive_planning_agent_aggregate_task","copilot_immersive_structured_model_picker","copilot_issue_list_show_more","copilot_no_floating_button","copilot_pipes_github_graphql_nodes","copilot_premium_request_quotas","copilot_read_shared_conversation","copilot_share_active_subthread","copilot_show_copilot_sub_issues_button_on_issues_page","copilot_spaces_as_attachments","copilot_spaces_ga","copilot_spark_allow_empty_commit","copilot_spark_loading_webgl","copilot_spark_progressive_error_handling","copilot_spark_read_iteration_history_from_git_v2","copilot_spark_single_user_iteration","copilot_spark_use_billing_headers","copilot_spark_write_iteration_history_to_git","copilot_stable_conversation_view","copilot_workbench_agent_seed_tool","copilot_workbench_cache","copilot_workbench_connection_reload_banner","copilot_workbench_preview_analytics","copilot_workbench_ratelimit_fallback","copilot_workbench_refresh_on_wsod","copilot_workbench_synthetic_generation","dashboard_public_preview","direct_to_salesforce","dotcom_chat_client_side_skills","failbot_report_error_react_apps_on_page","fgpat_permissions_selector_redesign","ghost_pilot_confidence_truncation_25","ghost_pilot_confidence_truncation_40","global_nav_copilot_a11y_fix","global_search_multi_orgs","global_sso_banner","hpc_improve_dom_insertion_observer","inp_reduced_threshold","insert_before_patch","issue_fields_report_usage","issues_copilot_cross_repo_assign","issues_copilot_repo_search_in_org","issues_expanded_file_types","issues_react_blur_item_picker_on_close","issues_react_bots_timeline_pagination","issues_react_include_bots_in_pickers","issues_react_prohibit_title_fallback","issues_react_remove_placeholders","issues_sticky_sidebar","kb_semantic_api_migration","lifecycle_label_name_updates","link_contact_sales_swp_marketo","marketing_pages_search_explore_provider","marketplace_async_recently_added","mcp_registry_install","memex_mwl_filter_field_delimiter","memex_roadmap_drag_style","migrate_toasts_to_banners_web_notifications","new_traffic_page_banner","one_click_merge_conflict","override_pulse_legacy_url","pinned_issue_fields","primer_react_segmented_control_tooltip","primer_react_unified_portal_root","pru_billing_page","record_sso_banner_metrics","releases_update_ref_selector","remove_child_patch","report_hydro_web_vitals","repos_insights_remove_new_url","repository_suggester_elastic_search","sample_network_conn_type","scheduled_reminders_updated_limits","site_homepage_collaborate_video","site_homepage_contentful","site_msbuild_webgl_hero","spark_commit_on_default_branch","spark_show_data_access_on_publish","spark_sync_repository_after_iteration","viewscreen_sandbox","webp_support","workbench_default_sonnet4","workbench_store_readonly"],"login":"FernandaBighi","copilotApiOverrideUrl":"https://api.individual.githubcopilot.com"}</script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_dompurify_dist_purify_es_mjs-0294cfa498e7.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_lodash-es__Stack_js-node_modules_lodash-es__Uint8Array_js-node_modules_l-4faaa6-95511fe13c4b.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_hydro-analytics-client_dist_analytics-client_js-node_modules_gith-c7919d-f0d6c180267d.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_tanstack_react-virtual_dist_esm_index_js-4f7c027617ef.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_catalyst_lib_index_js-node_modules_primer_styled-react_dist_index-d380a0-82f3868e5b2a.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_focus-visible_dist_-9130a4-faf8cb7afff9.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_fetch-headers_fetch-headers_ts-packages_history_history_ts-packages_promise-with-res-c5198c-ef8c20fb4804.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_copilot-chat_utils_copilot-local-storage_ts-4bd4f2203804.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_ref-selector_RefSelector_tsx-52b89ebfada2.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_commit-attribution_index_ts-packages_commit-checks-status_index_ts-packages_current--18e2dc-b3046fcc482e.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_code-view-shared_hooks_use-canonical-object_ts-packages_code-view-shared_hooks_use-f-37800a-23b41fa891e8.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_app-uuid_app-uuid_ts-packages_repos-file-tree-view_repos-file-tree-view_ts-276c634def9b.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/app_assets_modules_react-code-view_utilities_lines_ts-1281c585fc0b.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_code-view-shared_utilities_web-worker_ts-packages_code-view-shared_worker-jobs_debou-a85645-df70a4c9d58d.js.baixados" defer="defer"></script><script crossorigin="anonymous" type="application/javascript" src="./DTO_files/react-code-view-51c39dea034c.js.baixados" defer="defer"></script><link rel="dns-prefetch" href="https://github.githubassets.com/"><link rel="dns-prefetch" href="https://avatars.githubusercontent.com/"><link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/"><link rel="dns-prefetch" href="https://user-images.githubusercontent.com/"><link rel="preconnect" href="https://github.githubassets.com/" crossorigin=""><link rel="preconnect" href="https://avatars.githubusercontent.com/"><title>LojaVirtual_2025/DTO.md at main · maroquio/LojaVirtual_2025</title><meta name="route-pattern" content="/:user_id/:repository/tree/*name(/*path)" data-turbo-transient=""><meta name="route-controller" content="files" data-turbo-transient=""><meta name="route-action" content="disambiguate" data-turbo-transient=""><meta name="fetch-nonce" content="v2:fbea1888-b3aa-c205-8de9-5b9791464726"><meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb"><meta name="request-id" content="7C2D:1B98D6:758599:8AC407:68E53C4E" data-turbo-transient="true"><meta name="html-safe-nonce" content="e54ca0518bab598f3476a5b0654d681b1f86e12a1b111d9959f76037af321158" data-turbo-transient="true"><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9tYXJvcXVpby9Mb2phVmlydHVhbF8yMDI1L2Jsb2IvbWFpbi9EVE8ubWQiLCJyZXF1ZXN0X2lkIjoiN0MyRDoxQjk4RDY6NzU4NTk5OjhBQzQwNzo2OEU1M0M0RSIsInZpc2l0b3JfaWQiOiIyMDg1MzM1MjMyNDYwMTAwMTg2IiwicmVnaW9uX2VkZ2UiOiJicmF6aWxzb3V0aCIsInJlZ2lvbl9yZW5kZXIiOiJpYWQifQ==" data-turbo-transient="true"><meta name="visitor-hmac" content="356da7fb7849d39abbbacf9fe056b3e476731f20820b9384d6cd54e9ec8e34a9" data-turbo-transient="true"><meta name="hovercard-subject-tag" content="repository:992113407" data-turbo-transient=""><meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree,copilot" data-turbo-transient="true"><meta name="selected-link" value="repo_source" data-turbo-transient=""><link rel="assets" href="https://github.githubassets.com/"><meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I"><meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="octolytics-actor-id" content="198979522"><meta name="octolytics-actor-login" content="FernandaBighi"><meta name="octolytics-actor-hash" content="5944d58034e2e9a28d18d5900034ff5ab38218af54612e1b79c4aa1cec1c7827"><meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/files/disambiguate" data-turbo-transient="true"><meta name="user-login" content="FernandaBighi"><link rel="sudo-modal" href="https://github.com/sessions/sudo_modal"><meta name="turbo-cache-control" content="no-preview" data-turbo-transient=""><meta name="turbo-cache-control" content="no-cache" data-turbo-transient=""><meta data-hydrostats="publish"><meta name="go-import" content="github.com/maroquio/LojaVirtual_2025 git https://github.com/maroquio/LojaVirtual_2025.git"><meta name="octolytics-dimension-user_id" content="1246222"><meta name="octolytics-dimension-user_login" content="maroquio"><meta name="octolytics-dimension-repository_id" content="992113407"><meta name="octolytics-dimension-repository_nwo" content="maroquio/LojaVirtual_2025"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="992113407"><meta name="octolytics-dimension-repository_network_root_nwo" content="maroquio/LojaVirtual_2025"><meta name="turbo-body-classes" content="logged-in env-production page-responsive"><meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats"><meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors"><meta name="release" content="7194d4ad100e09f5290e6c0347e5e9ccf2898665"><meta name="ui-target" content="full"><link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000"><link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png"><link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg" data-base-href="https://github.githubassets.com/favicons/favicon"><meta name="theme-color" content="#1e2327"><meta name="color-scheme" content="light dark"><meta name="msapplication-TileImage" content="/windows-tile.png"><meta name="msapplication-TileColor" content="#ffffff"><link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials"><style type="text/css" id="ms-consent-banner-theme-styles"></style></head>

  <body class="logged-in env-production page-responsive" style="overflow-wrap: break-word; --dialog-scrollgutter: 13px;">
    <div data-turbo-body="" class="logged-in env-production page-responsive" style="word-wrap: break-word;">
        <div id="__primerPortalRoot__" role="region" style="z-index: 1000; position: absolute; width: 100%;" data-turbo-permanent=""></div>
      



    <div class="position-relative header-wrapper js-header-wrapper ">
      <a href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#start-of-content" data-skip-target-assigned="false" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/keyboard-shortcuts-dialog.2de9c7d6456a311fce49.module.css">

<react-partial partial-name="keyboard-shortcuts-dialog" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-none"></div><script type="application/json" id="__PRIMER_DATA_:r2m:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>





      

          

                  <header class="AppHeader" role="banner">
      <h2 class="sr-only">Navigation Menu</h2>


        

        <div class="AppHeader-globalBar pb-2 js-global-bar">
          <div class="AppHeader-globalBar-start responsive-context-region">
            <div class="">
                  <deferred-side-panel data-url="/_side-panels/global" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment" data-nonce="v2:fbea1888-b3aa-c205-8de9-5b9791464726" data-view-component="true"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
  
          <button aria-label="Open global navigation menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-118cd375-4be6-48aa-a1b9-bb13ab443ef5" id="dialog-show-dialog-118cd375-4be6-48aa-a1b9-bb13ab443ef5" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button p-0 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-three-bars Button-visual">
    <path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path>
</svg>
</button>

<dialog-helper>
  <dialog data-target="deferred-side-panel.panel" id="dialog-118cd375-4be6-48aa-a1b9-bb13ab443ef5" aria-modal="true" aria-labelledby="dialog-118cd375-4be6-48aa-a1b9-bb13ab443ef5-title" aria-describedby="dialog-118cd375-4be6-48aa-a1b9-bb13ab443ef5-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade Overlay--placement-left SidePanel Overlay--disableScroll">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-118cd375-4be6-48aa-a1b9-bb13ab443ef5-title">
        Global navigation
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12 1C5.923 1 1 5.923 1 12c0 4.867 3.149 8.979 7.521 10.436.55.096.756-.233.756-.522 0-.262-.013-1.128-.013-2.049-2.764.509-3.479-.674-3.699-1.292-.124-.317-.66-1.293-1.127-1.554-.385-.207-.936-.715-.014-.729.866-.014 1.485.797 1.691 1.128.99 1.663 2.571 1.196 3.204.907.096-.715.385-1.196.701-1.471-2.448-.275-5.005-1.224-5.005-5.432 0-1.196.426-2.186 1.128-2.956-.111-.275-.496-1.402.11-2.915 0 0 .921-.288 3.024 1.128a10.193 10.193 0 0 1 2.75-.371c.936 0 1.871.123 2.75.371 2.104-1.43 3.025-1.128 3.025-1.128.605 1.513.221 2.64.111 2.915.701.77 1.127 1.747 1.127 2.956 0 4.222-2.571 5.157-5.019 5.432.399.344.743 1.004.743 2.035 0 1.471-.014 2.654-.014 3.025 0 .289.206.632.756.522C19.851 20.979 23 16.854 23 12c0-6.077-4.922-11-11-11Z"></path>
</svg>
</div></div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-118cd375-4be6-48aa-a1b9-bb13ab443ef5" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="dialog-118cd375-4be6-48aa-a1b9-bb13ab443ef5-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body d-flex flex-column px-2">    <div data-view-component="true" class="d-flex flex-column mb-3">
        <nav aria-label="Site navigation" data-view-component="true" class="ActionList">
  
  <nav-list data-catalyst="">
    <ul data-target="nav-list.topLevelList" data-view-component="true" class="ActionListWrap">
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g d" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;HOME&quot;,&quot;label&quot;:null}" id="item-e0dddfc3-fbc1-461a-a331-b0aaab36ab03" href="https://github.com/dashboard" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-home">
    <path d="M6.906.664a1.749 1.749 0 0 1 2.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019A1.75 1.75 0 0 1 13.25 15h-3.5a.75.75 0 0 1-.75-.75V9H7v5.25a.75.75 0 0 1-.75.75h-3.5A1.75 1.75 0 0 1 1 13.25V6.23c0-.531.242-1.034.657-1.366l5.25-4.2Zm1.25 1.171a.25.25 0 0 0-.312 0l-5.25 4.2a.25.25 0 0 0-.094.196v7.019c0 .138.112.25.25.25H5.5V8.25a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 .75.75v5.25h2.75a.25.25 0 0 0 .25-.25V6.23a.25.25 0 0 0-.094-.195Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Home
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES&quot;,&quot;label&quot;:null}" id="item-aa943089-68fc-45cb-9c18-a1a3045d598c" href="https://github.com/issues" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS&quot;,&quot;label&quot;:null}" id="item-9fd12e9f-b34d-4786-b47e-3f9d97f0df83" href="https://github.com/pulls" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PROJECTS&quot;,&quot;label&quot;:null}" id="item-e88c0399-ab75-45d3-b7b6-40155f69ec5b" href="https://github.com/projects" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;DISCUSSIONS&quot;,&quot;label&quot;:null}" id="item-e7be2546-c21f-4b63-8843-8d557c5c8b4c" href="https://github.com/discussions" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Discussions
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;CODESPACES&quot;,&quot;label&quot;:null}" id="item-2e704377-4f43-4132-a43a-ab2361481658" href="https://github.com/codespaces" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Codespaces
</span>      
</a>
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider hide-whenRegular"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;COPILOT&quot;,&quot;label&quot;:null}" id="item-cfee76a9-19ce-428c-8c07-beaa7562c1a1" href="https://github.com/copilot" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copilot">
    <path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Copilot
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem hide-whenRegular">
    
    
    <a id="item-2eea78a6-bf1f-444f-9c26-1ca24723f103" href="https://github.com/copilot/spaces" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-space">
    <path d="M0 13.25V2.75C0 1.784.784 1 1.75 1H5c.551 0 1.07.26 1.4.7l.9 1.2a.25.25 0 0 0 .2.1h6.75c.966 0 1.75.784 1.75 1.75v3.638a.75.75 0 0 1-1.5 0V4.75a.25.25 0 0 0-.25-.25H7.5a1.75 1.75 0 0 1-1.4-.7l-.9-1.2a.25.25 0 0 0-.2-.1H1.75a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h5.663l.076.004a.75.75 0 0 1 0 1.492L7.413 15H1.75A1.75 1.75 0 0 1 0 13.25Z"></path><path d="M12.265 9.16a.248.248 0 0 1 .467 0l.237.649a3.726 3.726 0 0 0 2.219 2.218l.649.238a.249.249 0 0 1 0 .467l-.649.237a3.728 3.728 0 0 0-2.219 2.219l-.237.649a.249.249 0 0 1-.467 0l-.238-.649a3.726 3.726 0 0 0-2.218-2.219l-.649-.237a.248.248 0 0 1 0-.467l.649-.238a3.725 3.725 0 0 0 2.218-2.218l.238-.649Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Spaces
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem ActionListItem--hasSubItem hide-whenRegular">
    
    
    <button id="item-a14cfa53-a90c-4091-a29b-50cd8649a518" type="button" aria-expanded="false" data-action="
            click:nav-list#handleItemWithSubItemClick
            keydown:nav-list#handleItemWithSubItemKeydown
          " data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-download">
    <path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Download Copilot
</span>      
        <span class="ActionListItem-visual ActionListItem-action--trailing">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down ActionListItem-collapseIcon">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
        </span>
</button>
        <ul role="list" data-action="keydown:nav-list#handleItemWithSubItemKeydown" aria-labelledby="item-a14cfa53-a90c-4091-a29b-50cd8649a518" data-view-component="true" class="ActionList ActionList--subGroup">
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem--subItem ActionListItem">
    
    
    <a id="item-657be402-19c7-47e2-8e7b-f6719152f669" href="https://marketplace.visualstudio.com/items?itemName=GitHub.copilot" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          Visual Studio Code
</span>      
</a>
  
</li>

          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem--subItem ActionListItem">
    
    
    <a id="item-d8a4bb01-7e78-47e9-844b-def0f0daeff0" href="https://visualstudio.microsoft.com/github-copilot/" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          Visual Studio
</span>      
</a>
  
</li>

          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem--subItem ActionListItem">
    
    
    <a id="item-3bcb31d7-f7f6-4172-88db-c46cd2d39786" href="https://github.com/github/CopilotForXcode" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          Xcode
</span>      
</a>
  
</li>

          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem--subItem ActionListItem">
    
    
    <a id="item-0ff07b73-2904-4ade-a704-4147644a1e17" href="https://plugins.jetbrains.com/plugin/17718-github-copilot" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          JetBrains
</span>      
</a>
  
</li>

          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem--subItem ActionListItem">
    
    
    <a id="item-f25f7b19-79ad-4339-8b48-defb1e57e852" href="https://github.com/github/copilot.vim" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          Neovim
</span>      
</a>
  
</li>

          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem--subItem ActionListItem">
    
    
    <a id="item-80f0170b-e8e4-41d7-b4b7-6cb7eb80879a" href="https://docs.github.com/en/copilot/how-tos/set-up/installing-github-copilot-in-the-cli" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          CLI
</span>      
</a>
  
</li>

</ul>
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;EXPLORE&quot;,&quot;label&quot;:null}" id="item-c85e37c3-851e-46a3-acb4-7f217d18fa69" href="https://github.com/explore" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-telescope">
    <path d="M14.184 1.143v-.001l1.422 2.464a1.75 1.75 0 0 1-.757 2.451L3.104 11.713a1.75 1.75 0 0 1-2.275-.702l-.447-.775a1.75 1.75 0 0 1 .53-2.32L11.682.573a1.748 1.748 0 0 1 2.502.57Zm-4.709 9.32h-.001l2.644 3.863a.75.75 0 1 1-1.238.848l-1.881-2.75v2.826a.75.75 0 0 1-1.5 0v-2.826l-1.881 2.75a.75.75 0 1 1-1.238-.848l2.049-2.992a.746.746 0 0 1 .293-.253l1.809-.87a.749.749 0 0 1 .944.252ZM9.436 3.92h-.001l-4.97 3.39.942 1.63 5.42-2.61Zm3.091-2.108h.001l-1.85 1.26 1.505 2.605 2.016-.97a.247.247 0 0 0 .13-.151.247.247 0 0 0-.022-.199l-1.422-2.464a.253.253 0 0 0-.161-.119.254.254 0 0 0-.197.038ZM1.756 9.157a.25.25 0 0 0-.075.33l.447.775a.25.25 0 0 0 .325.1l1.598-.769-.83-1.436-1.465 1Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Explore
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;MARKETPLACE&quot;,&quot;label&quot;:null}" id="item-c0a88af0-e232-4b4c-bc9c-a41e45066ab4" href="https://github.com/marketplace" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gift">
    <path d="M2 2.75A2.75 2.75 0 0 1 4.75 0c.983 0 1.873.42 2.57 1.232.268.318.497.668.68 1.042.183-.375.411-.725.68-1.044C9.376.42 10.266 0 11.25 0a2.75 2.75 0 0 1 2.45 4h.55c.966 0 1.75.784 1.75 1.75v2c0 .698-.409 1.301-1 1.582v4.918A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V9.332C.409 9.05 0 8.448 0 7.75v-2C0 4.784.784 4 1.75 4h.55c-.192-.375-.3-.8-.3-1.25ZM7.25 9.5H2.5v4.75c0 .138.112.25.25.25h4.5Zm1.5 0v5h4.5a.25.25 0 0 0 .25-.25V9.5Zm0-4V8h5.5a.25.25 0 0 0 .25-.25v-2a.25.25 0 0 0-.25-.25Zm-7 0a.25.25 0 0 0-.25.25v2c0 .138.112.25.25.25h5.5V5.5h-5.5Zm3-4a1.25 1.25 0 0 0 0 2.5h2.309c-.233-.818-.542-1.401-.878-1.793-.43-.502-.915-.707-1.431-.707ZM8.941 4h2.309a1.25 1.25 0 0 0 0-2.5c-.516 0-1 .205-1.43.707-.337.392-.646.975-.879 1.793Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Marketplace
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;MCP_REGISTRY&quot;,&quot;label&quot;:null}" id="item-70d7f28c-34c9-4676-ab31-4501940bc8b2" href="https://github.com/mcp" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-mcp">
    <path d="M5.52 1.12a3.578 3.578 0 0 1 6.078 2.98 3.578 3.578 0 0 1 2.982 6.08l-3.292 3.293a.252.252 0 0 0 0 .354l.843.843a.749.749 0 1 1-1.06 1.06l-.844-.843a1.75 1.75 0 0 1 0-2.474L13.52 9.12a2.08 2.08 0 0 0 0-2.94 2.08 2.08 0 0 0-2.94 0L7.731 9.03A.75.75 0 0 1 6.67 7.97l2.85-2.85a2.08 2.08 0 0 0 0-2.94 2.08 2.08 0 0 0-2.94 0l-4.799 4.8A.75.75 0 0 1 .72 5.92Z"></path><path d="M7.52 3.12a.749.749 0 1 1 1.06 1.06L5.731 7.03A2.079 2.079 0 0 0 8.67 9.97l2.85-2.85a.749.749 0 1 1 1.06 1.06l-2.849 2.85A3.578 3.578 0 0 1 4.67 5.97Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          MCP Registry
</span>      
</a>
  
</li>

</ul>  </nav-list>
</nav>

        <div data-view-component="true" class="my-3 d-flex flex-justify-center height-full">
          <span data-view-component="true">
  <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>
</div>
</div>
      <div data-view-component="true" class="flex-1"></div>


      <div data-view-component="true" class="px-2">          <p class="color-fg-subtle text-small text-light">© 2025 GitHub, Inc.</p>

          <div data-view-component="true" class="d-flex flex-wrap text-small text-light">
              <a target="_blank" href="https://github.com/about" data-view-component="true" class="Link mr-2">About</a>
              <a target="_blank" href="https://github.blog/" data-view-component="true" class="Link mr-2">Blog</a>
              <a target="_blank" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link mr-2">Terms</a>
              <a target="_blank" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link mr-2">Privacy</a>
              <a target="_blank" href="https://github.com/security" data-view-component="true" class="Link mr-2">Security</a>
              <a target="_blank" href="https://www.githubstatus.com/" data-view-component="true" class="Link mr-3">Status</a>

</div></div>
</div>
      </scrollable-region>
      
</dialog></dialog-helper>


  <div data-show-on-forbidden-error="" hidden="">
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p><p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>
</include-fragment></deferred-side-panel>
            </div>

            <a class="AppHeader-logo ml-1 " href="https://github.com/" data-hotkey="g d" aria-label="Homepage " data-turbo="false" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}">
              <svg height="32" aria-hidden="true" viewBox="0 0 24 24" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle">
    <path d="M12 1C5.923 1 1 5.923 1 12c0 4.867 3.149 8.979 7.521 10.436.55.096.756-.233.756-.522 0-.262-.013-1.128-.013-2.049-2.764.509-3.479-.674-3.699-1.292-.124-.317-.66-1.293-1.127-1.554-.385-.207-.936-.715-.014-.729.866-.014 1.485.797 1.691 1.128.99 1.663 2.571 1.196 3.204.907.096-.715.385-1.196.701-1.471-2.448-.275-5.005-1.224-5.005-5.432 0-1.196.426-2.186 1.128-2.956-.111-.275-.496-1.402.11-2.915 0 0 .921-.288 3.024 1.128a10.193 10.193 0 0 1 2.75-.371c.936 0 1.871.123 2.75.371 2.104-1.43 3.025-1.128 3.025-1.128.605 1.513.221 2.64.111 2.915.701.77 1.127 1.747 1.127 2.956 0 4.222-2.571 5.157-5.019 5.432.399.344.743 1.004.743 2.035 0 1.471-.014 2.654-.014 3.025 0 .289.206.632.756.522C19.851 20.979 23 16.854 23 12c0-6.077-4.922-11-11-11Z"></path>
</svg>
            </a>

              <context-region-controller class="AppHeader-context responsive-context-region" data-max-items="5" data-catalyst="">
  <div class="AppHeader-context-full">
    <nav role="navigation" aria-label="GitHub Breadcrumb">
      
<context-region data-target="context-region-controller.contextRegion" role="list" data-action="context-region-changed:context-region-controller#crumbsChanged" data-catalyst="">
    <context-region-crumb data-crumb-id="contextregion-usercrumb-maroquio" data-targets="context-region.crumbs" data-label="maroquio" data-href="/maroquio" data-pre-rendered="" role="listitem" data-catalyst="">
      <a data-target="context-region-crumb.linkElement" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;maroquio&quot;,&quot;screen_size&quot;:&quot;full&quot;}" data-hovercard-type="user" data-hovercard-url="/users/maroquio/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maroquio" id="contextregion-usercrumb-maroquio-link" data-view-component="true" class="AppHeader-context-item" aria-keyshortcuts="Alt+ArrowUp">
        <span data-target="context-region-crumb.labelElement" class="AppHeader-context-item-label ">maroquio</span>

</a><tool-tip data-target="context-region-crumb.tooltip" for="contextregion-usercrumb-maroquio-link" popover="manual" class="sr-only" position="absolute" data-type="label" data-direction="s" hidden="" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>
          maroquio
        </tool-tip>
      <context-region-divider data-target="context-region-crumb.dividerElement" data-pre-rendered="" data-catalyst="">
  <span class="AppHeader-context-item-separator">
    <span class="sr-only">/</span>
    <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M10.956 1.27994L6.06418 14.7201L5 14.7201L9.89181 1.27994L10.956 1.27994Z" fill="currentcolor"></path>
    </svg>
  </span>
</context-region-divider>

    
        
      </context-region-crumb>

      <li data-target="context-region-controller.overflowMenuContainer context-region.overflowMenuContainer" role="listitem" hidden="">
        <action-menu data-target="context-region-controller.overflowActionMenu" data-select-variant="none" data-view-component="true" data-catalyst="" data-ready="true">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-menu-2b352a79-6b8d-4dd5-a893-952a666ad589-button" popovertarget="action-menu-2b352a79-6b8d-4dd5-a893-952a666ad589-overlay" aria-controls="action-menu-2b352a79-6b8d-4dd5-a893-952a666ad589-list" aria-haspopup="true" aria-labelledby="tooltip-37df7f74-dd36-480e-9a0e-e790ca036fa8" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-37df7f74-dd36-480e-9a0e-e790ca036fa8" for="action-menu-2b352a79-6b8d-4dd5-a893-952a666ad589-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Show more breadcrumb items</tool-tip>


<anchored-position data-target="action-menu.overlay" id="action-menu-2b352a79-6b8d-4dd5-a893-952a666ad589-overlay" anchor="action-menu-2b352a79-6b8d-4dd5-a893-952a666ad589-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 4px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list data-catalyst="">
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-2b352a79-6b8d-4dd5-a893-952a666ad589-button" id="action-menu-2b352a79-6b8d-4dd5-a893-952a666ad589-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="true" data-crumb-id="contextregion-usercrumb-maroquio" data-targets="context-region.overflowCrumbs action-list.items" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_overflow_menu_crumb&quot;,&quot;label&quot;:&quot;global-navigation&quot;}" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-86941d97-1c5d-4063-be5d-07b988d9e1ec" href="https://github.com/maroquio" role="menuitem" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          maroquio
</span>      
</a>
  
</li>
        <li hidden="true" data-crumb-id="contextregion-repositorycrumb-lojavirtual_2025" data-targets="context-region.overflowCrumbs action-list.items" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_overflow_menu_crumb&quot;,&quot;label&quot;:&quot;global-navigation&quot;}" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-8703e20d-5c54-4d19-b33e-a881eed02b6c" href="https://github.com/maroquio/LojaVirtual_2025" role="menuitem" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          LojaVirtual_2025
</span>      
</a>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu>
  <context-region-divider data-target="context-region-crumb.dividerElement" data-pre-rendered="" data-catalyst="">
  <span class="AppHeader-context-item-separator">
    <span class="sr-only">/</span>
    <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M10.956 1.27994L6.06418 14.7201L5 14.7201L9.89181 1.27994L10.956 1.27994Z" fill="currentcolor"></path>
    </svg>
  </span>
</context-region-divider>


      </li>
    <context-region-crumb data-crumb-id="contextregion-repositorycrumb-lojavirtual_2025" data-targets="context-region.crumbs" data-label="LojaVirtual_2025" data-href="/maroquio/LojaVirtual_2025" data-pre-rendered="" role="listitem" data-catalyst="">
      <a data-target="context-region-crumb.linkElement" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;LojaVirtual_2025&quot;,&quot;screen_size&quot;:&quot;full&quot;}" href="https://github.com/maroquio/LojaVirtual_2025" id="contextregion-repositorycrumb-lojavirtual_2025-link" data-view-component="true" class="AppHeader-context-item">
        <span data-target="context-region-crumb.labelElement" class="AppHeader-context-item-label ">LojaVirtual_2025</span>

</a><tool-tip data-target="context-region-crumb.tooltip" for="contextregion-repositorycrumb-lojavirtual_2025-link" popover="manual" class="sr-only" position="absolute" data-type="label" data-direction="s" hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>
          LojaVirtual_2025
        </tool-tip>
      <context-region-divider data-target="context-region-crumb.dividerElement" data-pre-rendered="" data-catalyst="">
  <span class="AppHeader-context-item-separator">
    <span class="sr-only">/</span>
    <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M10.956 1.27994L6.06418 14.7201L5 14.7201L9.89181 1.27994L10.956 1.27994Z" fill="currentcolor"></path>
    </svg>
  </span>
</context-region-divider>

    
        
      </context-region-crumb>

</context-region>

    </nav>
  </div>
</context-region-controller>

          </div>
          <div class="AppHeader-globalBar-end">
              <div class="AppHeader-search">
                  


<qbsearch-input class="search-input" data-scope="repo:maroquio/LojaVirtual_2025" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="GJVaklQ_nq98lWPagKFv5Y1mptNeFtJoeM_17mKXG7mdiCYkQlbrmkNV6ZIC0xQw96pUmV33MLQyRpScBNY5Pw" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="maroquio/LojaVirtual_2025" data-current-org="" data-current-owner="maroquio" data-logged-in="true" data-copilot-chat-enabled="true" data-nl-search-enabled="false" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">
      
            <button type="button" data-action="click:qbsearch-input#handleExpand" class="AppHeader-button AppHeader-search-whenNarrow" aria-label="Search or jump to…" aria-expanded="false" aria-haspopup="dialog">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </button>


<div class="AppHeader-search-whenRegular">
  <div class="AppHeader-search-wrap AppHeader-search-wrap--hasTrailing">
    <div class="AppHeader-search-control AppHeader-search-control-overflow">
      <label for="AppHeader-searchInput" aria-label="Search or jump to…" class="AppHeader-search-visual--leading">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
      </label>

                <button type="button" data-target="qbsearch-input.inputButton" data-action="click:qbsearch-input#handleExpand" class="AppHeader-searchButton form-control text-left color-fg-subtle no-wrap placeholder" data-hotkey="s,/" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;searchbar&quot;,&quot;context&quot;:&quot;global&quot;,&quot;tag&quot;:&quot;input&quot;,&quot;label&quot;:&quot;searchbar_input_global_navbar&quot;}" aria-describedby="search-error-message-flash">
            <div class="overflow-hidden">
              <span id="qb-input-query" data-target="qbsearch-input.inputButtonText">
                  Type <kbd class="AppHeader-search-kbd">/</kbd> to search
              </span>
            </div>
          </button>

    </div>


  </div>
</div>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-164429b8-e2a3-48e5-9dda-8252dc3119bd" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="copilot-error-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results" tabindex="-1"></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-164429b8-e2a3-48e5-9dda-8252dc3119bd" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="muGxBFAmjIx6rSv-bPCPghTjZvi0StWugf2xOBTO8k3pe-aojOUZ1K_gKP4Qg4EEP3eSDQkWxX3LYQy4yHdXOw">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="HoQN8alF36LKZqWNXaK_VUyEoSq73PKhkqY3vw8rsXwdwyapHzBtzPmPELtRsjXzLS1m_K_aF5aOdXW17vD2Cw">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="oSOLlMstmR9LkPL1JSh7lEuknu5UGXkFI7-Cj-9QfmngEJRLjwxPgzVT8_dxWTjQs5pBF3yOFkWPa6WOQ3N1cg" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input>  <input type="hidden" value="yQH23qzIbbbUoLmGb5ejfdu-7Sg0U5DV90DgyIU0O2hEQRRJrCGjWtE3IOWFMlAiVgsYjULeSq3j_nw8BZMTDw" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf">


              </div>

            
              <div class="AppHeader-CopilotChat hide-sm hide-md">
  <div class="d-flex">
    <react-partial-anchor data-catalyst="">
        <a href="https://github.com/copilot" data-target="react-partial-anchor.anchor" id="copilot-chat-header-button" aria-labelledby="tooltip-5c6b99c3-768e-45cf-ad14-b7575da7134f" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button AppHeader-buttonLeft">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copilot Button-visual">
    <path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-5c6b99c3-768e-45cf-ad14-b7575da7134f" for="copilot-chat-header-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Chat with Copilot</tool-tip>

      
    
        <script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_react-relay_index_js-065619a68bd6.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_comma-separated-tokens_index_js-node_modules_mdast-util-from-markdown_li-6db53e-7905a17e5b40.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_hastscript_lib_index_js-node_modules_mdast-util-gfm_lib_index_js-node_mo-2895d2-57ca8bf3ee61.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_tanstack_react-query_build_modern_useQuery_js-node_modules_diff_lib_index_mjs-1bcf85319d2e.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_remark-parse_lib_index_js-node_modules_unified_lib_index_js-75f3cad55f5a.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_lowlight_lib_all_js-node_modules_react-markdown_lib_index_js-node_module-5ac2ea-a3ad1da9eaac.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_accname_dist_access-ce77c7-d52adf73584a.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_fzy_js_index_js-node_modules_tanstack_react-query_build_modern_useMutati-22c8e6-bc1b91ed76b8.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_emoji-regex_index_js-node_modules_github_hydro-analytics-client_dist_ana-e6704d-cb0df7575265.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/vendors-node_modules_focus-visible_dist_focus-visible_js-node_modules_github_hotkey_dist_inde-e2ff11-d4fb7602eda8.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_copilot-chat_components_tracing_TraceProvider_tsx-fed3f2fdcee6.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_copilot-chat_utils_CopilotChatContext_tsx-packages_safe-html_VerifiedHTML_tsx-55ad16910c0d.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_item-picker_components_RepositoryPicker_tsx-99b664b764bf.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_copilot-markdown_MarkdownRenderer_tsx-616d424b0b25.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_code-view-shared_hooks_use-repos-analytics_ts-packages_code-view-shared_hooks_use-tr-fbe81a-59c112b6fb84.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_copilot-chat_components_ModelPicker_tsx-06e63f7baba5.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_copilot-chat_components_CopilotIconAnimation_tsx-4f0dd006fa0a.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_noop_noop_ts-packages_promise-with-resolvers-polyfill_promise-with-resolvers-polyfil-d772f1-cf2a0c8e360b.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/packages_copilot-chat_entry_ts-packages_use-debounce_use-debounce_ts-d6f05767cf0b.js.baixados" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./DTO_files/copilot-chat-69970666061f.js.baixados" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/packages_noop_noop_ts-packages_promise-with-resolvers-polyfill_promise-with-resolvers-polyfil-d772f1.c5529e8dc8d860fae659.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/copilot-chat.b9c6ea91ee9df8f32d5e.module.css">
        <link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/copilot-markdown-rendering-ddd978d4a7c0.css">
        <link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/primer-react.2ceb2571848317ce36f7.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/packages_noop_noop_ts-packages_promise-with-resolvers-polyfill_promise-with-resolvers-polyfil-d772f1.c5529e8dc8d860fae659.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/copilot-chat.b9c6ea91ee9df8f32d5e.module.css">

<react-partial partial-name="copilot-chat" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"currentTopic":{"id":992113407,"name":"LojaVirtual_2025","ownerLogin":"maroquio","ownerType":"User","readmePath":"README.md","description":null,"commitOID":"4a8b8d8da2ad587ff3d81c0e8baf0b7eb21bfd08","ref":"refs/heads/main","refInfo":{"name":"main","type":"branch"},"visibility":"public","languages":[{"name":"HTML","percent":49.1},{"name":"Python","percent":48.7},{"name":"JavaScript","percent":1.9},{"name":"CSS","percent":0.3}],"customInstructions":[],"defaultBranch":"main","ownerAvatarUrl":"https://avatars.githubusercontent.com/u/1246222?v=4"},"findFileWorkerPath":"/assets-cdn/worker/find-file-worker-9bd411a8e273.js","renderPopover":false,"renderBetaLabel":false,"chatIsVisible":true,"chatVisibleSettingPath":"/users/FernandaBighi/copilot_chat/settings/copilot_chat_visibility","ssoOrganizations":[],"apiVersion":"2025-05-01","agentsPath":"/github-copilot/chat/agents","apiURL":"https://api.individual.githubcopilot.com","currentUserLogin":"FernandaBighi","customInstructions":null,"renderKnowledgeBases":false,"customCopilotsEnabled":true,"optedInToPreviewFeatures":false,"optedInToUserFeedback":true,"renderAttachKnowledgeBaseHerePopover":true,"renderKnowledgeBaseAttachedToChatPopover":true,"personalInstructions":null,"reviewLab":false,"realIp":null,"scrollToTop":false,"hasCEorCBAccess":false,"licenseType":"licensed_limited","plan":"free","quotas":{"limits":{"premiumInteractions":0},"remaining":{"chat":500,"completions":4000,"premiumInteractions":0,"chatPercentage":100.0,"premiumInteractionsPercentage":0.0},"resetDate":"2025-10-19","overagesEnabled":false},"icebreakers":[{"type":"functional","data":[{"id":"create-bug-issue","message":"Hi Copilot! Could you please start a draft issue for a bug? Once you've created the draft issue, if you need more information, ask me 1-2 key questions. If you also think I should upload any information or images that would help write the bug issue, let me know.","titleHtml":"Create an issue for a bug","icon":"issue-opened","color":"var(--display-green-fgColor)"},{"id":"summarize-pulls","message":"Hi Copilot! Could you help summarize a pull request? I'd like to know its purpose and the key changes made. Please include details about the problem it solves, new features or functionality introduced, any breaking changes, testing done, and documentation updates. Thank you!","titleHtml":"Summarize a pull request","icon":"git-pull-request","color":"var(--display-green-fgColor)"},{"id":"code-feedback","message":"Hi Copilot! Please review my code for best practices, readability, performance, and potential bugs. First, prompt me to provide the link to the relevant GitHub repository or file. Then, offer concrete suggestions for improvement, explain any issues you discover, and provide example corrections where appropriate.","titleHtml":"Get code feedback","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"next-steps-issue","message":"Hi Copilot! Could you suggest the next actionable steps for an issue, based on either the provided issue link or a copy pasted description?","titleHtml":"Suggest next steps for an issue","icon":"issue-opened","color":"var(--display-green-fgColor)"},{"id":"understand-arch-diagram","message":"Hi Copilot! Could you please help me interpret this architecture diagram?","titleHtml":"Interpret an architecture diagram","icon":"eye","color":"var(--display-purple-fgColor)"},{"id":"create-profile-readme","message":"Hi Copilot! Please create a standout profile README for $$USERNAME$$. Ask me for any key details (such as my profession, top skills, favorite projects, or social links) that would help you personalize it.","titleHtml":"Create a profile README for me","icon":"rocket","color":"var(--display-pink-fgColor)"},{"id":"my-open-pulls","message":"Hi Copilot! Can you please find my open pull requests?","titleHtml":"My open pull requests","icon":"git-pull-request","color":"var(--display-green-fgColor)"},{"id":"make-pong","message":"Hi Copilot! Could you generate a simple Pong game utilizing HTML, CSS, and JavaScript? The player should control the left paddle with their mouse, and the right paddle should be controlled automatically by a basic AI. Make sure the game includes a bouncing ball and collision detection for paddles and walls. Please provide the code for all three components: the HTML file, the CSS file, and the JavaScript file directly within the chat window. Thanks!","titleHtml":"Make a Pong game","icon":"code","color":"var(--display-gray-fgColor)"}]},{"type":"instructional","data":[]},{"type":"interactional","data":[{"id":"to-do-app-local-storage","message":"Create a to-do list application with local storage functionality.","titleHtml":"To-do list with local storage","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"digital-clock-time-zones","message":"Create a digital clock that displays the current time in different time zones.","titleHtml":"A digital time zone clock","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"weather-dashboard-app","message":"Develop a weather dashboard that fetches data from a public weather API.","titleHtml":"Develop a weather dashboard","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"create-joke-generator","message":"Create a random joke generator using an external API.","titleHtml":"Create a joke generator","icon":"code","color":"var(--display-gray-fgColor)"}]}],"canShareThread":true,"thirdPartyMcpAllowed":true}}</script>
  <div data-target="react-partial.reactRoot"><div class="CopilotChat-module__CopilotChatContainer--fWXmM"></div><div class="PortalContainerUtils-module__chatPortalContainer--Otmle"></div><script type="application/json" id="__PRIMER_DATA_:r6a:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>



      </react-partial-anchor>
    <div class="position-relative">
      
        <react-partial-anchor data-catalyst="">
          <button id="global-copilot-menu-button" data-target="react-partial-anchor.anchor" aria-expanded="false" aria-labelledby="tooltip-fa1176e0-aaac-473c-9b7c-e2cb37b7847c" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button AppHeader-buttonRight" aria-haspopup="true">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down Button-visual">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</button><tool-tip id="tooltip-fa1176e0-aaac-473c-9b7c-e2cb37b7847c" for="global-copilot-menu-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Open Copilot…</tool-tip>

          
        
            <link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/global-copilot-menu.e8b96f8e81aaf397c759.module.css">

<react-partial partial-name="global-copilot-menu" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"repository":{"id":992113407,"name":"LojaVirtual_2025","ownerLogin":"maroquio"}}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-none"></div><script type="application/json" id="__PRIMER_DATA_:r2o:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>


          </react-partial-anchor>
    </div>
  </div>
</div>


            <div class="AppHeader-actions position-relative">
                 <react-partial-anchor data-catalyst="">
      <button id="global-create-menu-anchor" aria-label="Create something new" data-target="react-partial-anchor.anchor" type="button" data-view-component="true" class="AppHeader-button AppHeader-button--dropdown global-create-button Button--secondary Button--medium Button width-auto color-fg-muted" aria-describedby="tooltip-02e3a255-d97f-4254-9bd7-5b350180b78f" aria-expanded="false" aria-haspopup="true">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
      </span>
    <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg></span>
  </span>
</button><tool-tip id="tooltip-02e3a255-d97f-4254-9bd7-5b350180b78f" for="global-create-menu-anchor" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Create new…</tool-tip>

      
    
        <link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/global-create-menu.4d24ecb322134c573644.module.css">

<react-partial partial-name="global-create-menu" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"createRepo":true,"importRepo":true,"codespaces":true,"spark":false,"codingAgent":false,"gist":true,"createOrg":true,"createProject":false,"createProjectUrl":"/FernandaBighi?tab=projects","createLegacyProject":false,"createIssue":true,"org":null,"owner":"maroquio","repo":"LojaVirtual_2025"}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:r2s:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>


      </react-partial-anchor>

        
                <a href="https://github.com/issues" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-e0b15d92-f770-495f-af93-0d1d7ba93f12" aria-labelledby="tooltip-acf5b1f9-20f2-48a6-8d47-f3722b006b41" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened Button-visual">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
</a><tool-tip id="tooltip-acf5b1f9-20f2-48a6-8d47-f3722b006b41" for="icon-button-e0b15d92-f770-495f-af93-0d1d7ba93f12" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Your issues</tool-tip>

                <a href="https://github.com/pulls" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-1f5a5bc5-4c43-4bfb-a510-0b9ee48258d8" aria-labelledby="tooltip-a36fad34-20a7-4f0a-afd5-5217492dd1d3" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request Button-visual">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-a36fad34-20a7-4f0a-afd5-5217492dd1d3" for="icon-button-1f5a5bc5-4c43-4bfb-a510-0b9ee48258d8" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Your pull requests</tool-tip>

            </div>
            
              <notification-indicator data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTk4OTc5NTIyIiwidCI6MTc1OTg1MzY1M30=--523028ff4490f3991b1b5c50e22ef081513826b9713a4dcc19edb50472dfd1aa" data-indicator-mode="none" data-tooltip-global="You have unread notifications" data-tooltip-unavailable="Notifications are unavailable at the moment." data-tooltip-none="You have no unread notifications" data-header-redesign-enabled="true" data-fetch-indicator-src="/notifications/indicator" data-fetch-indicator-enabled="true" data-view-component="true" class="js-socket-channel" data-fetch-retry-delay-time="500" data-catalyst="">
    <a id="AppHeader-notifications-button" href="https://github.com/notifications" aria-labelledby="notification-indicator-tooltip" data-hotkey="g n" data-target="notification-indicator.link" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;NOTIFICATIONS_HEADER&quot;,&quot;label&quot;:&quot;icon:read&quot;}" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-inbox Button-visual">
    <path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path>
</svg>
</a>

    <tool-tip id="notification-indicator-tooltip" data-target="notification-indicator.tooltip" for="AppHeader-notifications-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>You have no unread notifications</tool-tip>
</notification-indicator>

            <div class="AppHeader-user">
              <deferred-side-panel data-url="/_side-panels/user?repository_id=992113407" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment" data-nonce="v2:fbea1888-b3aa-c205-8de9-5b9791464726" data-view-component="true"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
  
    <react-partial-anchor data-catalyst="">
  <button data-target="react-partial-anchor.anchor" data-login="FernandaBighi" aria-label="Open user navigation menu" type="button" data-view-component="true" class="Button--invisible Button--medium Button Button--invisible-noVisuals color-bg-transparent p-0" aria-expanded="false" aria-haspopup="true">  <span class="Button-content">
    <span class="Button-label"><img src="./DTO_files/198979522" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle"></span>
  </span>
</button>
  

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./DTO_files/global-user-nav-drawer.c2bc1ffb732493d0bf54.module.css">

<react-partial partial-name="global-user-nav-drawer" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"owner":{"login":"FernandaBighi","name":null,"avatarUrl":"https://avatars.githubusercontent.com/u/198979522?v=4"},"drawerId":"global-user-nav-drawer","lazyLoadItemDataFetchUrl":"/_side-panels/user.json","canAddAccount":true,"addAccountPath":"/login?add_account=1\u0026return_to=https%3A%2F%2Fgithub.com%2Fmaroquio%2FLojaVirtual_2025%2Ftree%2Fmain%2Fdtos","switchAccountPath":"/switch_account","loginAccountPath":"/login?add_account=1","projectsPath":"/FernandaBighi?tab=projects","gistsUrl":"https://gist.github.com/mine","docsUrl":"https://docs.github.com","yourEnterpriseUrl":null,"enterpriseSettingsUrl":null,"supportUrl":"https://support.github.com","showAccountSwitcher":true,"showCopilot":true,"showEnterprises":true,"showEnterprise":false,"showGists":true,"showOrganizations":true,"showSponsors":true,"showUpgrade":true,"showFeaturesPreviews":true,"showEnterpriseSettings":false,"createMenuProps":{"createRepo":true,"importRepo":true,"codespaces":true,"spark":false,"codingAgent":false,"gist":true,"createOrg":true,"createProject":false,"createProjectUrl":"/FernandaBighi?tab=projects","createLegacyProject":false,"createIssue":true,"org":null,"owner":"maroquio","repo":"LojaVirtual_2025"}}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:r2v:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>


  </react-partial-anchor>


  <div data-show-on-forbidden-error="" hidden="">
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p><p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>
</include-fragment></deferred-side-panel>
            </div>

            <div class="position-absolute mt-2">
                
<site-header-logged-in-user-menu data-catalyst="">

</site-header-logged-in-user-menu>

            </div>
          </div>
        </div>


        
            <div class="AppHeader-localBar">
              <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="https://github.com/maroquio/LojaVirtual_2025" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /maroquio/LojaVirtual_2025" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected" aria-current="page">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="https://github.com/maroquio/LojaVirtual_2025/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /maroquio/LojaVirtual_2025/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="https://github.com/maroquio/LojaVirtual_2025/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /maroquio/LojaVirtual_2025/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="https://github.com/maroquio/LojaVirtual_2025/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /maroquio/LojaVirtual_2025/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="https://github.com/maroquio/LojaVirtual_2025/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /maroquio/LojaVirtual_2025/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="https://github.com/maroquio/LojaVirtual_2025/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /maroquio/LojaVirtual_2025/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          </a><div data-show-on-forbidden-error="" hidden=""><a id="security-tab" href="https://github.com/maroquio/LojaVirtual_2025/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /maroquio/LojaVirtual_2025/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    </a><div class="Box"><a id="security-tab" href="https://github.com/maroquio/LojaVirtual_2025/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /maroquio/LojaVirtual_2025/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
  </a><div class="blankslate-container"><a id="security-tab" href="https://github.com/maroquio/LojaVirtual_2025/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /maroquio/LojaVirtual_2025/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    </a><div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2"><a id="security-tab" href="https://github.com/maroquio/LojaVirtual_2025/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /maroquio/LojaVirtual_2025/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p></a><p class="color-fg-muted my-2 mb-2 ws-normal"><a id="security-tab" href="https://github.com/maroquio/LojaVirtual_2025/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /maroquio/LojaVirtual_2025/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">There was an error while loading. </a><a class="Link--inTextBlock" data-turbo="false" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>


    
</li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="https://github.com/maroquio/LojaVirtual_2025/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /maroquio/LojaVirtual_2025/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true" data-catalyst="" data-ready="true">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-menu-2a36e471-d750-4d47-9ee2-ee49f2d0c6d2-button" popovertarget="action-menu-2a36e471-d750-4d47-9ee2-ee49f2d0c6d2-overlay" aria-controls="action-menu-2a36e471-d750-4d47-9ee2-ee49f2d0c6d2-list" aria-haspopup="true" aria-labelledby="tooltip-e8841397-3ff3-4fe1-b00a-37d7ad09f3ce" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-e8841397-3ff3-4fe1-b00a-37d7ad09f3ce" for="action-menu-2a36e471-d750-4d47-9ee2-ee49f2d0c6d2-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Additional navigation options</tool-tip>


<anchored-position data-target="action-menu.overlay" id="action-menu-2a36e471-d750-4d47-9ee2-ee49f2d0c6d2-overlay" anchor="action-menu-2a36e471-d750-4d47-9ee2-ee49f2d0c6d2-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 35.9886px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list data-catalyst="">
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-2a36e471-d750-4d47-9ee2-ee49f2d0c6d2-button" id="action-menu-2a36e471-d750-4d47-9ee2-ee49f2d0c6d2-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="" data-menu-item="i0code-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-566e6fca-99c3-40d2-a440-ca324d5212fd" href="https://github.com/maroquio/LojaVirtual_2025" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i1issues-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-fee61b0c-b1e6-4cd4-af9d-cf1e17175e73" href="https://github.com/maroquio/LojaVirtual_2025/issues" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i2pull-requests-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-53fc2d93-5694-4883-a6d1-831070983750" href="https://github.com/maroquio/LojaVirtual_2025/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i3actions-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-76e273ed-9b89-4dc4-b2dc-945d9c0af35a" href="https://github.com/maroquio/LojaVirtual_2025/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Actions
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i4projects-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-22ad0de9-2394-4650-a7da-73d5d1be4cb0" href="https://github.com/maroquio/LojaVirtual_2025/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i5security-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-d14e70db-4563-45fe-a45d-1b25745c855b" href="https://github.com/maroquio/LojaVirtual_2025/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Security
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i6insights-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-38fa9c1b-c77b-4edb-a2ec-c1709f424e73" href="https://github.com/maroquio/LojaVirtual_2025/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Insights
</span>      
</a>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu></div>
</nav>
              
            </div>
    </header>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a class="Link--inTextBlock" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a class="Link--inTextBlock" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a class="Link--inTextBlock" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md">Reload</a> to refresh your session.</span>

    <button id="icon-button-aed80ce2-432e-4e76-a2bb-a846f59ff490" aria-labelledby="tooltip-0804f663-2c19-4c0c-a447-735575885878" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-0804f663-2c19-4c0c-a447-735575885878" for="icon-button-aed80ce2-432e-4e76-a2bb-a846f59ff490" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Dismiss alert</tool-tip>


  
</div>
        
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" class="flash-container" data-turbo-replace="">




  <template class="js-flash-template"></template>
</div>


    
  <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTk4OTc5NTIyIiwidCI6MTc1OTg1MzY1M30=--523028ff4490f3991b1b5c50e22ef081513826b9713a4dcc19edb50472dfd1aa" data-view-component="true" class="js-socket-channel" data-refresh-delay="500" data-catalyst="" data-throttle-delay="5000"></notification-shelf-watcher>
  <div hidden="" data-initial="" data-target="notification-shelf-watcher.placeholder"></div>






  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="" data-project-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
      






    
  <div id="repository-container-header" data-turbo-replace="" hidden=""></div>




<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content ">
      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".,Mod+Alt+.">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+.,Shift+&gt;,&gt;" target="_blank" rel="noopener noreferrer">Open in a new github.dev tab</a>
    <a class="d-none" data-hotkey=",,Mod+Alt+," target="_blank" href="https://github.com/codespaces/new/maroquio/LojaVirtual_2025/tree/main?resume=1">Open in codespace</a>




    
      
    








<react-app app-name="react-code-view" initial-path="/maroquio/LojaVirtual_2025/tree/main/dtos" style="display: block; min-height: calc(100vh - 64px);" data-attempted-ssr="true" data-ssr="true" data-lazy="false" data-alternate="false" data-data-router-enabled="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"allShortcutsEnabled":true,"path":"dtos","repo":{"id":992113407,"defaultBranch":"main","name":"LojaVirtual_2025","ownerLogin":"maroquio","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2025-05-28T13:31:25.000-03:00","ownerAvatar":"https://avatars.githubusercontent.com/u/1246222?v=4","public":true,"private":false,"isOrgOwned":false},"currentUser":{"id":198979522,"login":"FernandaBighi","userEmail":"fernandabb909@gmail.com"},"refInfo":{"name":"main","listCacheKey":"v0:1748449892.0","canEdit":true,"refType":"branch","currentOid":"4a8b8d8da2ad587ff3d81c0e8baf0b7eb21bfd08"},"tree":{"items":[{"name":"__init__.py","path":"dtos/__init__.py","contentType":"file"},{"name":"base_dto.py","path":"dtos/base_dto.py","contentType":"file"},{"name":"categoria_dto.py","path":"dtos/categoria_dto.py","contentType":"file"}],"templateDirectorySuggestionUrl":null,"readme":null,"totalCount":3,"showBranchInfobar":false},"fileTree":{"":{"items":[{"name":".claude","path":".claude","contentType":"directory"},{"name":".vscode","path":".vscode","contentType":"directory"},{"name":"data","path":"data","contentType":"directory"},{"name":"dtos","path":"dtos","contentType":"directory"},{"name":"model","path":"model","contentType":"directory"},{"name":"repo","path":"repo","contentType":"directory"},{"name":"routes","path":"routes","contentType":"directory"},{"name":"sql","path":"sql","contentType":"directory"},{"name":"static","path":"static","contentType":"directory"},{"name":"templates","path":"templates","contentType":"directory"},{"name":"util","path":"util","contentType":"directory"},{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":"AUTH.md","path":"AUTH.md","contentType":"file"},{"name":"CLAUDE.md","path":"CLAUDE.md","contentType":"file"},{"name":"DTO.md","path":"DTO.md","contentType":"file"},{"name":"FOTOS.md","path":"FOTOS.md","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"TOASTS.md","path":"TOASTS.md","contentType":"file"},{"name":"dados.db","path":"dados.db","contentType":"file"},{"name":"main.py","path":"main.py","contentType":"file"},{"name":"package-lock.json","path":"package-lock.json","contentType":"file"},{"name":"package.json","path":"package.json","contentType":"file"},{"name":"requirements.txt","path":"requirements.txt","contentType":"file"}],"totalCount":23}},"fileTreeProcessingTime":29.674547999999998,"foldersToFetch":[],"treeExpanded":true,"symbolsExpanded":false,"copilotSWEAgentEnabled":false,"csrf_tokens":{"/maroquio/LojaVirtual_2025/branches":{"post":"JFk-iaZAhE_dyaHHCzvHzP4z2S6d2b11ekmdUDp9t6BszaPgJPj7rx-IfdieoVNPK8l_WrjbHizkyZ-5pdcriw"},"/maroquio/LojaVirtual_2025/branches/fetch_and_merge/main":{"post":"iWve-MaWqeGGnHDPSlUaTdRJHXCYul2mVUa3iQ406BEK5N3Jocr8zR3gqK65i8jp8LvGqAKs43u68kmNDgREbA"},"/maroquio/LojaVirtual_2025/branches/fetch_and_merge/main?discard_changes=true":{"post":"YcyslYcmZvzsrZ8D5Ei3ruuUaSG7X09zjm4Pca9MBtbiQ6-k4Hoz0HfRR2IXlmUKz2ay-SFJ8a5h2vF1r3yqqw"}}},"title":"LojaVirtual_2025/dtos at main · maroquio/LojaVirtual_2025","appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-9bd411a8e273.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-410714137fc9.js","githubDevUrl":"https://github.dev/","enabled_features":{"code_nav_ui_events":false,"react_blob_overlay":true,"accessible_code_button":true}}}</script>
  <div data-target="react-app.reactRoot"><meta data-hydrostats="publish"> <!-- --> <!-- --> <button hidden="" data-testid="header-permalink-button" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="y,Shift+Y"></button><button hidden="" data-hotkey="y,Shift+Y"></button><div><div style="--spacing:var(--spacing-none)" class="prc-PageLayout-PageLayoutRoot-1zlEO"><div class="prc-PageLayout-PageLayoutWrapper-s2ao4" data-width="full"><div class="prc-PageLayout-PageLayoutContent-jzDMn"><div tabindex="0" class="Box-sc-g0xbh4-0 gISSDQ"><div class="prc-PageLayout-PaneWrapper-nGO0U ReposFileTreePane-module__Pane--D26Sw ReposFileTreePane-module__HidePane--a07q8" style="--offset-header:0px;--spacing-row:var(--spacing-none);--spacing-column:var(--spacing-none)" data-is-hidden="false" data-position="start" data-sticky="true"><div class="prc-PageLayout-HorizontalDivider-CYLp5 prc-PageLayout-PaneHorizontalDivider-4exOb" data-variant="none" data-position="start" style="--spacing-divider:var(--spacing-none);--spacing:var(--spacing-none)"></div><div class="prc-PageLayout-Pane-Vl5LI" data-resizable="true" style="--spacing:var(--spacing-none);--pane-min-width:256px;--pane-max-width:calc(100vw - var(--pane-max-width-diff));--pane-width-size:var(--pane-width-large);--pane-width:320px"><div><div id="repos-file-tree" class="Box-sc-g0xbh4-0 bNhwaa"><div class="ReposFileTreePane-module__Box_1--ZT_4S"><div class="Box-sc-g0xbh4-0 jfIeyl"><h2 class="use-tree-pane-module__Heading--iI_ad prc-Heading-Heading-6CmGO"><button data-component="IconButton" type="button" data-testid="collapse-file-tree-button" aria-expanded="true" aria-controls="repos-file-tree" class="prc-Button-ButtonBase-c50BI position-relative ExpandFileTreeButton-module__expandButton--oKI1R fgColor-muted prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-describedby=":R756mplab:-loading-announcement" aria-labelledby=":R156mplab:" data-hotkey="Control+b"><svg aria-hidden="true" focusable="false" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="se" aria-hidden="true" id=":R156mplab:" popover="auto">Collapse file tree</span><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+b"></button></h2><h2 class="Box-sc-g0xbh4-0 kOkWgo prc-Heading-Heading-6CmGO">Files</h2></div><div class="ReposFileTreePane-module__Box_2--RgzGf"><div class="ReposFileTreePane-module__Box_3--XDLn8"><button style="min-width:0" type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" aria-label="main branch" data-testid="anchor-button" class="prc-Button-ButtonBase-c50BI react-repos-tree-pane-ref-selector width-full ref-selector-class RefSelectorAnchoredOverlay-module__RefSelectorOverlayBtn--D34zl" data-loading="false" data-size="medium" data-variant="default" aria-describedby="ref-picker-repos-header-ref-selector-loading-announcement" id="ref-picker-repos-header-ref-selector" data-hotkey="w"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayContainer--mCbv8"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayHeader--D4cnZ"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="ref-selector-button-text-container RefSelectorAnchoredOverlay-module__RefSelectorBtnTextContainer--yO402"><span class="RefSelectorAnchoredOverlay-module__RefSelectorText--bxVhQ">&nbsp;<!-- -->main</span></div></div></span><span data-component="trailingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-testid="ref-selector-hotkey-button" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="w"></button></div><div class="ReposFileTreePane-module__Box_4--TLAAU"><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-c50BI ReposFileTreePane-module__IconButton--fpuBk prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":R6q6mplab:-loading-announcement" aria-labelledby=":Rq6mplab:" href="https://github.com/maroquio/LojaVirtual_2025/new/main" data-discover="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="n" aria-hidden="true" id=":Rq6mplab:" popover="auto">Add file</span><button data-component="IconButton" type="button" class="Box-sc-g0xbh4-0 dPUXSa prc-Button-ButtonBase-c50BI SearchButton-module__IconButton--kxA3Q prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":Rra6mplab:-loading-announcement" aria-labelledby=":R3a6mplab:" data-hotkey="/"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":R3a6mplab:" popover="auto">Search this repository</span><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="/"></button></div></div></div><div class="Box-sc-g0xbh4-0 ReposFileTreePane-module__FileResultsList--YEf_n"><span class="d-flex FileResultsList-module__FilesSearchBox--fSAh3 TextInput-wrapper prc-components-TextInputWrapper-i1ofR prc-components-TextInputBaseWrapper-ueK9q" data-leading-visual="true" data-trailing-visual="true" aria-busy="false"><span class="TextInput-icon" id=":R5amplab:" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autocorrect="off" spellcheck="false" placeholder="Go to file" aria-describedby=":R5amplab: :R5amplabH1:" data-component="input" class="prc-components-Input-Ic-y8" value=""><span class="TextInput-icon" id=":R5amplabH1:" aria-hidden="true"><kbd>t</kbd></span></span></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="t,Shift+T"></button><button hidden="" data-hotkey="t,Shift+T"></button><div class="ReposFileTreePane-module__Box_8--KVzCi"></div><div class="Box-sc-g0xbh4-0 ReposFileTreePane-module__Box_5--cckih"><div><div class="react-tree-show-tree-items"><div class="ReposFileTreeView-module__Box--bDodO" data-testid="repos-file-tree-container"><nav aria-label="File Tree Navigation"><span class="prc-src-InternalVisuallyHidden-nlR9R" role="status" aria-live="polite" aria-atomic="true"></span><ul role="tree" aria-label="Files" data-truncate-text="true" class="prc-TreeView-TreeViewRootUlStyles-eZtxW"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id=".claude-item" role="treeitem" aria-labelledby=":r30:" aria-describedby=":r31:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":r30:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r31:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>.claude</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id=".vscode-item" role="treeitem" aria-labelledby=":r34:" aria-describedby=":r35:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":r34:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r35:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>.vscode</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="data-item" role="treeitem" aria-labelledby=":r38:" aria-describedby=":r39:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":r38:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r39:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>data</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="dtos-item" role="treeitem" aria-labelledby=":r3c:" aria-describedby=":r3d:" aria-level="1" aria-expanded="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M6 8.825c-.2 0-.4-.1-.5-.2l-3.3-3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l2.7 2.7 2.7-2.7c.3-.3.8-.3 1.1 0 .3.3.3.8 0 1.1l-3.2 3.2c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":r3c:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r3d:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-open-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M.513 1.513A1.75 1.75 0 0 1 1.75 1h3.5c.55 0 1.07.26 1.4.7l.9 1.2a.25.25 0 0 0 .2.1H13a1 1 0 0 1 1 1v.5H2.75a.75.75 0 0 0 0 1.5h11.978a1 1 0 0 1 .994 1.117L15 13.25A1.75 1.75 0 0 1 13.25 15H1.75A1.75 1.75 0 0 1 0 13.25V2.75c0-.464.184-.91.513-1.237Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>dtos</span></span></div></div><ul role="group" aria-label="dtos" style="list-style: none; padding: 0px; margin: 0px;"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="dtos/__init__.py-item" role="treeitem" aria-labelledby=":r3g:" aria-describedby=":r3h:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-KPSSL"></div></div></div><div id=":r3g:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r3h:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>__init__.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="dtos/base_dto.py-item" role="treeitem" aria-labelledby=":r3k:" aria-describedby=":r3l:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-KPSSL"></div></div></div><div id=":r3k:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r3l:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>base_dto.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="dtos/categoria_dto.py-item" role="treeitem" aria-labelledby=":r3o:" aria-describedby=":r3p:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-KPSSL"></div></div></div><div id=":r3o:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r3p:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>categoria_dto.py</span></span></div></div></li></ul></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="model-item" role="treeitem" aria-labelledby=":r3s:" aria-describedby=":r3t:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":r3s:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r3t:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>model</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="repo-item" role="treeitem" aria-labelledby=":r40:" aria-describedby=":r41:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":r40:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r41:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>repo</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="routes-item" role="treeitem" aria-labelledby=":r44:" aria-describedby=":r45:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":r44:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r45:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>routes</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="sql-item" role="treeitem" aria-labelledby=":r48:" aria-describedby=":r49:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":r48:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r49:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>sql</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="static-item" role="treeitem" aria-labelledby=":r4c:" aria-describedby=":r4d:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":r4c:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r4d:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>static</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="templates-item" role="treeitem" aria-labelledby=":r4g:" aria-describedby=":r4h:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":r4g:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r4h:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>templates</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="util-item" role="treeitem" aria-labelledby=":r4k:" aria-describedby=":r4l:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":r4k:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r4l:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>util</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id=".gitignore-item" role="treeitem" aria-labelledby=":r4o:" aria-describedby=":r4p:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r4o:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r4p:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>.gitignore</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="AUTH.md-item" role="treeitem" aria-labelledby=":r4s:" aria-describedby=":r4t:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r4s:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r4t:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>AUTH.md</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="CLAUDE.md-item" role="treeitem" aria-labelledby=":r50:" aria-describedby=":r51:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r50:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r51:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>CLAUDE.md</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="DTO.md-item" role="treeitem" aria-labelledby=":r54:" aria-describedby=":r55:" aria-level="1" aria-selected="false" aria-current="true"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r54:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r55:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>DTO.md</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="FOTOS.md-item" role="treeitem" aria-labelledby=":r58:" aria-describedby=":r59:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r58:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r59:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>FOTOS.md</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="README.md-item" role="treeitem" aria-labelledby=":r5c:" aria-describedby=":r5d:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r5c:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r5d:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>README.md</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="TOASTS.md-item" role="treeitem" aria-labelledby=":r5g:" aria-describedby=":r5h:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r5g:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r5h:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>TOASTS.md</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="dados.db-item" role="treeitem" aria-labelledby=":r5k:" aria-describedby=":r5l:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r5k:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r5l:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>dados.db</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="main.py-item" role="treeitem" aria-labelledby=":r5o:" aria-describedby=":r5p:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r5o:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r5p:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>main.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="package-lock.json-item" role="treeitem" aria-labelledby=":r5s:" aria-describedby=":r5t:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r5s:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r5t:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>package-lock.json</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="package.json-item" role="treeitem" aria-labelledby=":r60:" aria-describedby=":r61:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r60:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r61:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>package.json</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="-1" id="requirements.txt-item" role="treeitem" aria-labelledby=":r64:" aria-describedby=":r65:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r64:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":r65:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>requirements.txt</span></span></div></div></li></ul></nav></div></div></div></div></div></div></div><div class="prc-PageLayout-VerticalDivider-4A4Qm prc-PageLayout-PaneVerticalDivider-1c9vy" data-variant="line" data-position="start" style="--spacing:var(--spacing-none)"><div role="slider" aria-label="Draggable pane splitter" aria-valuemin="256" aria-valuemax="488" aria-valuenow="320" aria-valuetext="Pane width 320 pixels" tabindex="0" class="Box-sc-g0xbh4-0 bHLmSv"></div></div></div></div><div class="prc-PageLayout-ContentWrapper-b-QRo CodeView-module__SplitPageLayout_Content--qxR1C" data-is-hidden="false"><div class="prc-PageLayout-Content--F7-I" data-width="full" style="--spacing:var(--spacing-none)"><div data-selector="repos-split-pane-content" tabindex="0" class="Box-sc-g0xbh4-0 leYMvG"><div class="Box-sc-g0xbh4-0 KMPzq"><div class="container CodeViewHeader-module__Box--PofRM"><div class="px-3 pt-3 pb-0" id="StickyHeader" style="position: sticky;"><div class="CodeViewHeader-module__Box_1--KpLzV"><div class="CodeViewHeader-module__Box_2--xzDOt"><div class="CodeViewHeader-module__Box_6--iStzT"><div class="Box-sc-g0xbh4-0 cEytCf"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb--wide-heading" id="repos-header-breadcrumb--wide" class="Box-sc-g0xbh4-0 fzFXnm"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading" id="repos-header-breadcrumb--wide-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 iMnkmv"><li class="Box-sc-g0xbh4-0 ghzDag"><a class="Box-sc-g0xbh4-0 kHuKdh prc-Link-Link-85e08" sx="[object Object]" data-testid="breadcrumbs-repo-link" href="https://github.com/maroquio/LojaVirtual_2025/tree/main" data-discover="true">LojaVirtual_2025</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 ghzDag"><span class="Box-sc-g0xbh4-0 hzJBof prc-Text-Text-0ima0" aria-hidden="true">/</span><h1 class="Box-sc-g0xbh4-0 jGhzSQ prc-Heading-Heading-6CmGO" tabindex="-1" id="file-name-id-wide">DTO.md</h1></div><button data-component="IconButton" type="button" class="prc-Button-ButtonBase-c50BI ml-2 prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby=":Rvb9lab:-loading-announcement" aria-labelledby=":R3b9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span class="CopyToClipboardButton-module__tooltip--HDUYz prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-label="Copy path" aria-hidden="true" id=":R3b9lab:" popover="auto">Copy path</span></div></div><div class="react-code-view-header-element--wide"><div class="CodeViewHeader-module__Box_7--FZfkg"><div class="d-flex gap-2"> <button type="button" data-hotkey="b,Shift+B,Control+/ Control+b" class="Box-sc-g0xbh4-0 fjrFuv prc-Button-ButtonBase-c50BI NavigationMenu-module__Button--SJihq" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":r6b:-loading-announcement"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x">Blame</span></span></button><button hidden="" data-testid="" data-hotkey="b,Shift+B,Control+/ Control+b" data-hotkey-scope="read-only-cursor-text-area"></button><button data-component="IconButton" type="button" data-testid="more-file-actions-button-nav-menu-wide" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI js-blob-dropdown-click NavigationMenu-module__IconButton--NqJ_L prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":r6c:-loading-announcement" aria-labelledby=":r6e:" id=":r6c:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":r6e:" popover="auto">More file actions</span> </div></div></div><div class="react-code-view-header-element--narrow"><div class="CodeViewHeader-module__Box_7--FZfkg"><div class="d-flex gap-2"> <button type="button" data-hotkey="b,Shift+B,Control+/ Control+b" class="Box-sc-g0xbh4-0 fjrFuv prc-Button-ButtonBase-c50BI NavigationMenu-module__Button--SJihq" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":r6g:-loading-announcement"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x">Blame</span></span></button><button hidden="" data-testid="" data-hotkey="b,Shift+B,Control+/ Control+b" data-hotkey-scope="read-only-cursor-text-area"></button><button data-component="IconButton" type="button" data-testid="more-file-actions-button-nav-menu-narrow" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI js-blob-dropdown-click NavigationMenu-module__IconButton--NqJ_L prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":r6h:-loading-announcement" aria-labelledby=":r6j:" id=":r6h:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":r6j:" popover="auto">More file actions</span> </div></div></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0 dJxjrT react-code-view-bottom-padding"> <div class="BlobTopBanners-module__Box--g_bGk"></div>   </div><div class="Box-sc-g0xbh4-0 dJxjrT">   <button hidden="" data-testid="" data-hotkey="r,Shift+R" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="r,Shift+R"></button><div class="d-flex flex-column border rounded-2 mb-3 pl-1"><div class="LatestCommit-module__Box--Fimpo"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading">Latest commit</h2><div data-testid="latest-commit" class="LatestCommit-module__Box_1--aQ5OG"><div class="CommitAttribution-module__CommitAttributionContainer--Si80C"><div data-testid="author-avatar" class="Box-sc-g0xbh4-0 AuthorAvatar-module__AuthorAvatarContainer--Z1TF8"><a class="prc-Link-Link-85e08" href="https://github.com/maroquio" data-testid="avatar-icon-link" data-hovercard-url="/users/maroquio/hovercard" aria-keyshortcuts="Alt+ArrowUp"><img data-component="Avatar" class="AuthorAvatar-module__authorAvatarImage--bQzij prc-Avatar-Avatar-ZRS-m" alt="maroquio" width="20" height="20" src="./DTO_files/1246222" data-testid="github-avatar" aria-label="maroquio" style="--avatarSize-regular: 20px;"></a><a class="Box-sc-g0xbh4-0 gLSgdJ AuthorAvatar-module__authorHoverableLink--vw9qe prc-Link-Link-85e08" data-muted="true" href="https://github.com/maroquio/LojaVirtual_2025/commits?author=maroquio" aria-label="commits by maroquio" data-hovercard-url="/users/maroquio/hovercard" aria-keyshortcuts="Alt+ArrowUp">maroquio</a></div><span class=""></span></div><div class="d-none d-sm-flex LatestCommit-module__Box_2--JDY37"><div class="Truncate flex-items-center f5"><span class="Truncate-text prc-Text-Text-0ima0" data-testid="latest-commit-html"><a href="https://github.com/maroquio/LojaVirtual_2025/commit/d573799a2f8ef2cf1d85dd07f115b4cb03e013cb" class="Link--secondary" data-pjax="true" data-hovercard-url="/maroquio/LojaVirtual_2025/commit/d573799a2f8ef2cf1d85dd07f115b4cb03e013cb/hovercard" aria-keyshortcuts="Alt+ArrowUp">dtos</a></span></div></div><span class="d-flex d-sm-none fgColor-muted f6"><relative-time tense="past" datetime="2025-09-29T20:47:33.000Z" title="Sep 29, 2025, 5:47 PM GMT-3"><template shadowrootmode="open">last week</template>Sep 29, 2025</relative-time></span></div><div class="d-flex flex-shrink-0 gap-2"><div data-testid="latest-commit-details" class="d-none d-sm-flex flex-items-center"><span class="d-flex flex-nowrap fgColor-muted f6"><a class="Link--secondary prc-Link-Link-85e08" aria-label="Commit d573799" data-hovercard-url="/maroquio/LojaVirtual_2025/commit/d573799a2f8ef2cf1d85dd07f115b4cb03e013cb/hovercard" href="https://github.com/maroquio/LojaVirtual_2025/commit/d573799a2f8ef2cf1d85dd07f115b4cb03e013cb" data-discover="true" aria-keyshortcuts="Alt+ArrowUp">d573799</a>&nbsp;·&nbsp;<relative-time tense="past" datetime="2025-09-29T20:47:33.000Z" title="Sep 29, 2025, 5:47 PM GMT-3"><template shadowrootmode="open">last week</template>Sep 29, 2025</relative-time></span></div><div class="d-flex gap-2"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading">History</h2><a href="https://github.com/maroquio/LojaVirtual_2025/commits/main/DTO.md" class="prc-Button-ButtonBase-c50BI d-none d-lg-flex LinkButton-module__code-view-link-button--thtqc flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":r6l:-loading-announcement"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x"><span class="fgColor-default">History</span></span></span></a><div class="d-sm-none"><button data-component="IconButton" type="button" aria-pressed="false" aria-expanded="false" data-testid="latest-commit-details-toggle" class="prc-Button-ButtonBase-c50BI LatestCommit-module__IconButton--Zxaob prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby=":r7v:-loading-announcement" aria-labelledby=":r7u:"><svg aria-hidden="true" focusable="false" class="octicon octicon-ellipsis" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 5.75C0 4.784.784 4 1.75 4h12.5c.966 0 1.75.784 1.75 1.75v4.5A1.75 1.75 0 0 1 14.25 12H1.75A1.75 1.75 0 0 1 0 10.25ZM12 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2ZM7 8a1 1 0 1 0 2 0 1 1 0 0 0-2 0ZM4 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="s" aria-hidden="true" id=":r7u:" popover="auto">Open commit details</span></div><div class="d-flex d-lg-none"><span role="tooltip" aria-label="History" id="history-icon-button-tooltip" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-n"><a aria-label="View commit history for this file." href="https://github.com/maroquio/LojaVirtual_2025/commits/main/DTO.md" class="prc-Button-ButtonBase-c50BI LinkButton-module__code-view-link-button--thtqc flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":r6n:-loading-announcement history-icon-button-tooltip"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a></span></div></div></div></div></div><div class="Box-sc-g0xbh4-0 ldRxiI"><div class="Box-sc-g0xbh4-0 fVkfyA container"><div class="Box-sc-g0xbh4-0 gNAmSV react-code-size-details-banner"><div class="react-code-size-details-banner CodeSizeDetails-module__Box--QdxnQ"><div class="text-mono CodeSizeDetails-module__Box_1--_uFDs"><div data-testid="blob-size" class="CodeSizeDetails-module__Truncate_1--er0Uk prc-Truncate-Truncate-A9Wn6" data-inline="true" title="32.2 KB" style="--truncate-max-width: 100%;"><span>1269 lines (977 loc) · 32.2 KB</span></div></div></div></div><div class="Box-sc-g0xbh4-0 jdLMhu react-blob-view-header-sticky" id="repos-sticky-header"><div class="BlobViewHeader-module__Box--pvsIA"><div class="react-blob-sticky-header"><div class="Box-sc-g0xbh4-0 cWyMqi"><div class="FileNameStickyHeader-module__Box_5--xBJ2J"><div class="Box-sc-g0xbh4-0 fHind"><nav data-testid="breadcrumbs" aria-labelledby="sticky-breadcrumb-heading" id="sticky-breadcrumb" class="Box-sc-g0xbh4-0 fzFXnm"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading" id="sticky-breadcrumb-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 iMnkmv"><li class="Box-sc-g0xbh4-0 ghzDag"><a class="Box-sc-g0xbh4-0 kHuKdh prc-Link-Link-85e08" sx="[object Object]" data-testid="breadcrumbs-repo-link" href="https://github.com/maroquio/LojaVirtual_2025/tree/main" data-discover="true">LojaVirtual_2025</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 ghzDag"><span class="Box-sc-g0xbh4-0 oDtgN prc-Text-Text-0ima0" aria-hidden="true">/</span><h1 class="Box-sc-g0xbh4-0 dnZoUW prc-Heading-Heading-6CmGO" tabindex="-1" id="sticky-file-name-id">DTO.md</h1></div></div><button type="button" class="prc-Button-ButtonBase-c50BI FileNameStickyHeader-module__Button--SaiiH FileNameStickyHeader-module__GoToTopButton--9lB4x" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":r6o:-loading-announcement"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-arrow-up" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M3.47 7.78a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0l4.25 4.25a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018L9 4.81v7.44a.75.75 0 0 1-1.5 0V4.81L4.53 7.78a.75.75 0 0 1-1.06 0Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x">Top</span></span></button></div></div></div><div class="Box-sc-g0xbh4-0 dhuhek BlobViewHeader-module__Box_1--PPihg"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading">File metadata and controls</h2><div class="BlobViewHeader-module__Box_2--G_jCG"><ul aria-label="File view" class="prc-SegmentedControl-SegmentedControl-e7570 BlobTabButtons-module__SegmentedControl--JMGov" data-size="small"><li class="prc-SegmentedControl-Item-7Aq6h" data-selected=""><button aria-current="true" class="prc-SegmentedControl-Button-ojWXD" type="button" data-hotkey="Control+/ Control+p" style="--separator-color: transparent;"><span class="prc-SegmentedControl-Content-gnQ4n segmentedControl-content"><div class="prc-SegmentedControl-Text-c5gSh segmentedControl-text" data-text="Preview">Preview</div></span></button></li><li class="prc-SegmentedControl-Item-7Aq6h"><button aria-current="false" class="prc-SegmentedControl-Button-ojWXD" type="button" data-hotkey="Control+/ Control+c" style="--separator-color: var(--borderColor-default, var(--color-border-default, #d0d7de));"><span class="prc-SegmentedControl-Content-gnQ4n segmentedControl-content"><div class="prc-SegmentedControl-Text-c5gSh segmentedControl-text" data-text="Code">Code</div></span></button></li><li class="prc-SegmentedControl-Item-7Aq6h"><button aria-current="false" class="prc-SegmentedControl-Button-ojWXD" type="button" data-hotkey="b,Shift+B,Control+/ Control+b" style="--separator-color: var(--borderColor-default, var(--color-border-default, #d0d7de));"><span class="prc-SegmentedControl-Content-gnQ4n segmentedControl-content"><div class="prc-SegmentedControl-Text-c5gSh segmentedControl-text" data-text="Blame">Blame</div></span></button></li></ul><button hidden="" data-testid="" data-hotkey="Control+/ Control+c" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="" data-hotkey="b,Shift+B,Control+/ Control+b" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="" data-hotkey="Control+/ Control+p" data-hotkey-scope="read-only-cursor-text-area"></button><div class="react-code-size-details-in-header CodeSizeDetails-module__Box--QdxnQ"><div class="text-mono CodeSizeDetails-module__Box_1--_uFDs"><div data-testid="blob-size" class="CodeSizeDetails-module__Truncate_1--er0Uk prc-Truncate-Truncate-A9Wn6" data-inline="true" title="32.2 KB" style="--truncate-max-width: 100%;"><span>1269 lines (977 loc) · 32.2 KB</span></div></div></div></div><div class="BlobViewHeader-module__Box_3--Kvpex"><button hidden="" data-testid="" data-hotkey="Control+Shift+&gt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+Shift+&gt;"></button><button hidden="" data-testid="" data-hotkey="Control+Shift+&lt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+Shift+&lt;"></button><button data-component="IconButton" type="button" data-testid="copilot-ask-menu" class="prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby="blob-view-header-copilot-icon-loading-announcement" aria-labelledby=":r6p:" id="blob-view-header-copilot-icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="n" aria-hidden="true" id=":r6p:" popover="auto">Ask Copilot about this file</span><div class="react-blob-header-edit-and-raw-actions BlobViewHeader-module__Box_4--vFP89"><div class="prc-ButtonGroup-ButtonGroup-vcMeG"><div><a href="https://github.com/maroquio/LojaVirtual_2025/raw/refs/heads/main/DTO.md" data-testid="raw-button" data-hotkey="Control+/ Control+r" class="prc-Button-ButtonBase-c50BI LinkButton-sc-1v6zkmg-0 iwmTUC BlobViewHeader-module__LinkButton--DMph4" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":r6r:-loading-announcement"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x">Raw</span></span></a></div><div><button data-component="IconButton" type="button" data-testid="copy-raw-button" data-hotkey="Control+Shift+C" class="prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":r6t:-loading-announcement" aria-labelledby=":r6s:"><svg aria-hidden="true" focusable="false" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="n" aria-hidden="true" id=":r6s:" popover="auto">Copy raw file</span></div><div><button data-component="IconButton" type="button" data-testid="download-raw-button" data-hotkey="Control+Shift+S" class="Box-sc-g0xbh4-0 ivobqY prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":r6v:-loading-announcement" aria-labelledby=":r6u:"><svg aria-hidden="true" focusable="false" class="octicon octicon-download" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="n" aria-hidden="true" id=":r6u:" popover="auto">Download raw file</span></div></div><button hidden="" data-testid="raw-button-shortcut" data-hotkey="Control+/ Control+r" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="copy-raw-button-shortcut" data-hotkey="Control+Shift+C" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="download-raw-button-shortcut" data-hotkey="Control+Shift+S" data-hotkey-scope="read-only-cursor-text-area"></button><a class="js-github-dev-shortcut d-none prc-Link-Link-85e08" data-hotkey="., Control+Shift+/" href="https://github.dev/"></a><button hidden="" data-testid="" data-hotkey="., Control+Shift+/" data-hotkey-scope="read-only-cursor-text-area"></button><a class="js-github-dev-new-tab-shortcut d-none prc-Link-Link-85e08" data-hotkey="Shift+.,Shift+&gt;,&gt;" href="https://github.dev/" target="_blank"></a><button hidden="" data-testid="" data-hotkey="Shift+.,Shift+&gt;,&gt;" data-hotkey-scope="read-only-cursor-text-area"></button><div class="prc-ButtonGroup-ButtonGroup-vcMeG"><div><a sx="[object Object]" data-component="IconButton" type="button" data-hotkey="e,Shift+E" data-testid="edit-button" class="Box-sc-g0xbh4-0 iCOsHh prc-Button-ButtonBase-c50BI BlobViewHeader-module__IconButton_1--MzNlL prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":r71:-loading-announcement" aria-labelledby=":r70:" href="https://github.com/maroquio/LojaVirtual_2025/edit/main/DTO.md" data-discover="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-pencil" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":r70:" popover="auto">Edit the file in your fork of this project</span></div><div><button data-component="IconButton" type="button" data-testid="more-edit-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":r72:-loading-announcement" aria-labelledby=":r74:" id=":r72:"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":r74:" popover="auto">More edit options</span></div></div><button hidden="" data-testid="" data-hotkey="e,Shift+E" data-hotkey-scope="read-only-cursor-text-area"></button></div><button data-component="IconButton" type="button" aria-pressed="false" class="Box-sc-g0xbh4-0 yaMnG prc-Button-ButtonBase-c50BI TableOfContents-module__IconButton--RCaNg prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby=":r7p:-loading-announcement" aria-labelledby=":r7o:"><svg aria-hidden="true" focusable="false" class="octicon octicon-list-unordered" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M5.75 2.5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5ZM2 14a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-6a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM2 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="n" aria-hidden="true" id=":r7o:" popover="auto">Outline</span><div class="react-blob-header-edit-and-raw-actions-combined"><button data-component="IconButton" type="button" title="More file actions" data-testid="more-file-actions-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI js-blob-dropdown-click BlobViewHeader-module__IconButton--uO1fA prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby=":r78:-loading-announcement" aria-labelledby=":r7a:" id=":r78:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":r7a:" popover="auto">Edit and raw actions</span></div></div></div></div><div></div></div><div class="Box-sc-g0xbh4-0 hGyMdv"><section aria-labelledby="file-name-id-wide file-name-id-mobile" class="Box-sc-g0xbh4-0 fGqKFv"><div class="Box-sc-g0xbh4-0 eoaCFS js-snippet-clipboard-copy-unpositioned undefined" data-hpc="true"><article class="markdown-body entry-content container-lg" itemprop="text"><div class="markdown-heading" dir="auto"><h1 tabindex="-1" class="heading-element" dir="auto">📋 Manual de Implementação de DTOs (Data Transfer Objects)</h1><a id="user-content--manual-de-implementação-de-dtos-data-transfer-objects" class="anchor" aria-label="Permalink: 📋 Manual de Implementação de DTOs (Data Transfer Objects)" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#-manual-de-implementa%C3%A7%C3%A3o-de-dtos-data-transfer-objects"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">🎯 Objetivo</h2><a id="user-content--objetivo" class="anchor" aria-label="Permalink: 🎯 Objetivo" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#-objetivo"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Este manual fornece um guia completo para implementar DTOs (Data Transfer Objects) usando Pydantic em projetos Python, seguindo o padrão de excelência do projeto CaseBem. É voltado para projetos que <strong>não possuem nenhuma estrutura de DTOs ou validações implementada</strong>.</p>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">📚 Índice</h2><a id="user-content--índice" class="anchor" aria-label="Permalink: 📚 Índice" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#-%C3%ADndice"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ol dir="auto">
<li><a href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#o-que-s%C3%A3o-dtos">O que são DTOs?</a></li>
<li><a href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#por-que-usar-dtos">Por que usar DTOs?</a></li>
<li><a href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#arquitetura-proposta">Arquitetura Proposta</a></li>
<li><a href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#passo-a-passo-de-implementa%C3%A7%C3%A3o">Passo a Passo de Implementação</a></li>
<li><a href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#exemplos-pr%C3%A1ticos">Exemplos Práticos</a></li>
<li><a href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#boas-pr%C3%A1ticas">Boas Práticas</a></li>
<li><a href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#troubleshooting">Troubleshooting</a></li>
</ol>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">🔍 O que são DTOs?</h2><a id="user-content--o-que-são-dtos" class="anchor" aria-label="Permalink: 🔍 O que são DTOs?" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#-o-que-s%C3%A3o-dtos"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong>DTOs (Data Transfer Objects)</strong> são objetos simples usados para transferir dados entre camadas da aplicação, especialmente entre a camada de apresentação (APIs, formulários) e a camada de lógica de negócio.</p>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Características dos DTOs:</h3><a id="user-content-características-dos-dtos" class="anchor" aria-label="Permalink: Características dos DTOs:" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#caracter%C3%ADsticas-dos-dtos"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul dir="auto">
<li>✅ Apenas dados (sem lógica de negócio complexa)</li>
<li>✅ Validação automática de tipos e formatos</li>
<li>✅ Conversão automática de dados</li>
<li>✅ Documentação integrada (schemas JSON/OpenAPI)</li>
<li>✅ Reutilizáveis em diferentes contextos</li>
</ul>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">💡 Por que usar DTOs?</h2><a id="user-content--por-que-usar-dtos" class="anchor" aria-label="Permalink: 💡 Por que usar DTOs?" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#-por-que-usar-dtos"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">1. <strong>Validação Automática</strong></h3><a id="user-content-1-validação-automática" class="anchor" aria-label="Permalink: 1. Validação Automática" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#1-valida%C3%A7%C3%A3o-autom%C3%A1tica"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-c"># Sem DTO</span>
<span class="pl-k">def</span> <span class="pl-en">criar_usuario</span>(<span class="pl-s1">nome</span>: <span class="pl-smi">str</span>, <span class="pl-s1">email</span>: <span class="pl-smi">str</span>, <span class="pl-s1">idade</span>: <span class="pl-smi">int</span>):
    <span class="pl-k">if</span> <span class="pl-c1">not</span> <span class="pl-s1">nome</span> <span class="pl-c1">or</span> <span class="pl-en">len</span>(<span class="pl-s1">nome</span>) <span class="pl-c1">&lt;</span> <span class="pl-c1">2</span>:
        <span class="pl-k">raise</span> <span class="pl-en">ValueError</span>(<span class="pl-s">"Nome inválido"</span>)
    <span class="pl-k">if</span> <span class="pl-s">"@"</span> <span class="pl-c1"><span class="pl-c1">not</span> <span class="pl-c1">in</span></span> <span class="pl-s1">email</span>:
        <span class="pl-k">raise</span> <span class="pl-en">ValueError</span>(<span class="pl-s">"Email inválido"</span>)
    <span class="pl-k">if</span> <span class="pl-s1">idade</span> <span class="pl-c1">&lt;</span> <span class="pl-c1">18</span>:
        <span class="pl-k">raise</span> <span class="pl-en">ValueError</span>(<span class="pl-s">"Idade inválida"</span>)
    <span class="pl-c"># ... mais validações ...</span>

<span class="pl-c"># Com DTO</span>
<span class="pl-k">class</span> <span class="pl-v">UsuarioDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s1">nome</span>: <span class="pl-smi">str</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(<span class="pl-s1">min_length</span><span class="pl-c1">=</span><span class="pl-c1">2</span>)
    <span class="pl-s1">email</span>: <span class="pl-smi">EmailStr</span>
    <span class="pl-s1">idade</span>: <span class="pl-smi">int</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(<span class="pl-s1">ge</span><span class="pl-c1">=</span><span class="pl-c1">18</span>)

<span class="pl-c"># Validação automática!</span>
<span class="pl-s1">usuario</span> <span class="pl-c1">=</span> <span class="pl-en">UsuarioDTO</span>(<span class="pl-s1">nome</span><span class="pl-c1">=</span><span class="pl-s">"João"</span>, <span class="pl-s1">email</span><span class="pl-c1">=</span><span class="pl-s">"joao@email.com"</span>, <span class="pl-s1">idade</span><span class="pl-c1">=</span><span class="pl-c1">25</span>)</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="# Sem DTO
def criar_usuario(nome: str, email: str, idade: int):
    if not nome or len(nome) &lt; 2:
        raise ValueError(&quot;Nome inválido&quot;)
    if &quot;@&quot; not in email:
        raise ValueError(&quot;Email inválido&quot;)
    if idade &lt; 18:
        raise ValueError(&quot;Idade inválida&quot;)
    # ... mais validações ...

# Com DTO
class UsuarioDTO(BaseDTO):
    nome: str = Field(min_length=2)
    email: EmailStr
    idade: int = Field(ge=18)

# Validação automática!
usuario = UsuarioDTO(nome=&quot;João&quot;, email=&quot;joao@email.com&quot;, idade=25)" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">2. <strong>Separação de Responsabilidades</strong></h3><a id="user-content-2-separação-de-responsabilidades" class="anchor" aria-label="Permalink: 2. Separação de Responsabilidades" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#2-separa%C3%A7%C3%A3o-de-responsabilidades"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul dir="auto">
<li><strong>Model (DB):</strong> Representa dados no banco de dados</li>
<li><strong>DTO:</strong> Representa dados da API/formulário</li>
<li><strong>Service:</strong> Lógica de negócio</li>
</ul>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">3. <strong>Documentação Automática</strong></h3><a id="user-content-3-documentação-automática" class="anchor" aria-label="Permalink: 3. Documentação Automática" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#3-documenta%C3%A7%C3%A3o-autom%C3%A1tica"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul dir="auto">
<li>Geração automática de schema OpenAPI</li>
<li>Exemplos de uso integrados</li>
<li>Validações documentadas</li>
</ul>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">4. <strong>Segurança</strong></h3><a id="user-content-4-segurança" class="anchor" aria-label="Permalink: 4. Segurança" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#4-seguran%C3%A7a"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul dir="auto">
<li>Controle preciso de quais campos podem ser recebidos</li>
<li>Prevenção de mass assignment</li>
<li>Sanitização automática de dados</li>
</ul>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">🏗️ Arquitetura Proposta</h2><a id="user-content-️-arquitetura-proposta" class="anchor" aria-label="Permalink: 🏗️ Arquitetura Proposta" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#%EF%B8%8F-arquitetura-proposta"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>seu-projeto/
├── dtos/
│   ├── __init__.py          # Imports centralizados
│   ├── base_dto.py          # Classe base para todos os DTOs
│   ├── usuario_dtos.py      # DTOs relacionados a usuários
│   ├── produto_dtos.py      # DTOs relacionados a produtos
│   └── pedido_dtos.py       # DTOs relacionados a pedidos
│
├── util/
│   └── validacoes_dto.py    # Funções de validação reutilizáveis
│
└── model/
    └── usuario_model.py      # Models do banco de dados
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="seu-projeto/
├── dtos/
│   ├── __init__.py          # Imports centralizados
│   ├── base_dto.py          # Classe base para todos os DTOs
│   ├── usuario_dtos.py      # DTOs relacionados a usuários
│   ├── produto_dtos.py      # DTOs relacionados a produtos
│   └── pedido_dtos.py       # DTOs relacionados a pedidos
│
├── util/
│   └── validacoes_dto.py    # Funções de validação reutilizáveis
│
└── model/
    └── usuario_model.py      # Models do banco de dados" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Princípios da Arquitetura:</h3><a id="user-content-princípios-da-arquitetura" class="anchor" aria-label="Permalink: Princípios da Arquitetura:" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#princ%C3%ADpios-da-arquitetura"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ol dir="auto">
<li><strong>Um arquivo por domínio:</strong> Agrupe DTOs relacionados</li>
<li><strong>BaseDTO:</strong> Classe base com configurações comuns</li>
<li><strong>Validações centralizadas:</strong> Reutilize funções de validação</li>
<li><strong>Imports facilitados:</strong> Use <code>__init__.py</code> para simplificar imports</li>
</ol>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">📝 Passo a Passo de Implementação</h2><a id="user-content--passo-a-passo-de-implementação" class="anchor" aria-label="Permalink: 📝 Passo a Passo de Implementação" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#-passo-a-passo-de-implementa%C3%A7%C3%A3o"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><strong>PASSO 1: Instalar Dependências</strong></h3><a id="user-content-passo-1-instalar-dependências" class="anchor" aria-label="Permalink: PASSO 1: Instalar Dependências" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#passo-1-instalar-depend%C3%AAncias"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>pip install pydantic[email]</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="pip install pydantic[email]" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Adicione ao <code>requirements.txt</code>:</strong></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>pydantic&gt;=2.0.0
email-validator&gt;=2.0.0
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="pydantic&gt;=2.0.0
email-validator&gt;=2.0.0" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><strong>PASSO 2: Criar Estrutura de Diretórios</strong></h3><a id="user-content-passo-2-criar-estrutura-de-diretórios" class="anchor" aria-label="Permalink: PASSO 2: Criar Estrutura de Diretórios" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#passo-2-criar-estrutura-de-diret%C3%B3rios"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>mkdir -p dtos
mkdir -p util
touch dtos/__init__.py
touch dtos/base_dto.py
touch util/validacoes_dto.py</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="mkdir -p dtos
mkdir -p util
touch dtos/__init__.py
touch dtos/base_dto.py
touch util/validacoes_dto.py" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><strong>PASSO 3: Implementar Exceção Personalizada</strong></h3><a id="user-content-passo-3-implementar-exceção-personalizada" class="anchor" aria-label="Permalink: PASSO 3: Implementar Exceção Personalizada" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#passo-3-implementar-exce%C3%A7%C3%A3o-personalizada"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong>Arquivo: <code>util/validacoes_dto.py</code></strong></p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-s">"""</span>
<span class="pl-s">Biblioteca centralizada de validações para DTOs</span>
<span class="pl-s">"""</span>

<span class="pl-k">class</span> <span class="pl-v">ValidacaoError</span>(<span class="pl-v">ValueError</span>):
    <span class="pl-s">"""Exceção personalizada para erros de validação"""</span>
    <span class="pl-k">pass</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="&quot;&quot;&quot;
Biblioteca centralizada de validações para DTOs
&quot;&quot;&quot;

class ValidacaoError(ValueError):
    &quot;&quot;&quot;Exceção personalizada para erros de validação&quot;&quot;&quot;
    pass" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><strong>PASSO 4: Criar Funções de Validação</strong></h3><a id="user-content-passo-4-criar-funções-de-validação" class="anchor" aria-label="Permalink: PASSO 4: Criar Funções de Validação" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#passo-4-criar-fun%C3%A7%C3%B5es-de-valida%C3%A7%C3%A3o"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong>Adicione ao arquivo <code>util/validacoes_dto.py</code>:</strong></p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">import</span> <span class="pl-s1">re</span>
<span class="pl-k">from</span> <span class="pl-s1">typing</span> <span class="pl-k">import</span> <span class="pl-v">Optional</span>
<span class="pl-k">from</span> <span class="pl-s1">decimal</span> <span class="pl-k">import</span> <span class="pl-v">Decimal</span>

<span class="pl-k">def</span> <span class="pl-en">validar_texto_obrigatorio</span>(
    <span class="pl-s1">texto</span>: <span class="pl-smi">str</span>,
    <span class="pl-s1">campo</span>: <span class="pl-smi">str</span> <span class="pl-c1">=</span> <span class="pl-s">"Campo"</span>,
    <span class="pl-s1">min_chars</span>: <span class="pl-smi">int</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span>,
    <span class="pl-s1">max_chars</span>: <span class="pl-smi">int</span> <span class="pl-c1">=</span> <span class="pl-c1">255</span>
) <span class="pl-c1">-&gt;</span> <span class="pl-smi">str</span>:
    <span class="pl-s">"""</span>
<span class="pl-s">    Valida texto obrigatório com limites de tamanho</span>
<span class="pl-s"></span>
<span class="pl-s">    Args:</span>
<span class="pl-s">        texto: Texto a ser validado</span>
<span class="pl-s">        campo: Nome do campo (para mensagens de erro)</span>
<span class="pl-s">        min_chars: Tamanho mínimo</span>
<span class="pl-s">        max_chars: Tamanho máximo</span>
<span class="pl-s"></span>
<span class="pl-s">    Returns:</span>
<span class="pl-s">        Texto validado e limpo</span>
<span class="pl-s"></span>
<span class="pl-s">    Raises:</span>
<span class="pl-s">        ValidacaoError: Se validação falhar</span>
<span class="pl-s">    """</span>
    <span class="pl-k">if</span> <span class="pl-c1">not</span> <span class="pl-s1">texto</span> <span class="pl-c1">or</span> <span class="pl-c1">not</span> <span class="pl-s1">texto</span>.<span class="pl-c1">strip</span>():
        <span class="pl-k">raise</span> <span class="pl-en">ValidacaoError</span>(<span class="pl-s">f'<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">campo</span><span class="pl-kos">}</span></span> é obrigatório'</span>)

    <span class="pl-s1">texto_limpo</span> <span class="pl-c1">=</span> <span class="pl-s1">texto</span>.<span class="pl-c1">strip</span>()

    <span class="pl-k">if</span> <span class="pl-en">len</span>(<span class="pl-s1">texto_limpo</span>) <span class="pl-c1">&lt;</span> <span class="pl-s1">min_chars</span>:
        <span class="pl-k">raise</span> <span class="pl-en">ValidacaoError</span>(<span class="pl-s">f'<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">campo</span><span class="pl-kos">}</span></span> deve ter pelo menos <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">min_chars</span><span class="pl-kos">}</span></span> caracteres'</span>)

    <span class="pl-k">if</span> <span class="pl-en">len</span>(<span class="pl-s1">texto_limpo</span>) <span class="pl-c1">&gt;</span> <span class="pl-s1">max_chars</span>:
        <span class="pl-k">raise</span> <span class="pl-en">ValidacaoError</span>(<span class="pl-s">f'<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">campo</span><span class="pl-kos">}</span></span> deve ter no máximo <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">max_chars</span><span class="pl-kos">}</span></span> caracteres'</span>)

    <span class="pl-k">return</span> <span class="pl-s1">texto_limpo</span>


<span class="pl-k">def</span> <span class="pl-en">validar_texto_opcional</span>(
    <span class="pl-s1">texto</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>],
    <span class="pl-s1">max_chars</span>: <span class="pl-smi">int</span> <span class="pl-c1">=</span> <span class="pl-c1">500</span>
) <span class="pl-c1">-&gt;</span> <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>]:
    <span class="pl-s">"""</span>
<span class="pl-s">    Valida texto opcional</span>
<span class="pl-s"></span>
<span class="pl-s">    Args:</span>
<span class="pl-s">        texto: Texto a ser validado (pode ser None)</span>
<span class="pl-s">        max_chars: Tamanho máximo</span>
<span class="pl-s"></span>
<span class="pl-s">    Returns:</span>
<span class="pl-s">        Texto validado ou None</span>
<span class="pl-s"></span>
<span class="pl-s">    Raises:</span>
<span class="pl-s">        ValidacaoError: Se texto exceder tamanho máximo</span>
<span class="pl-s">    """</span>
    <span class="pl-k">if</span> <span class="pl-c1">not</span> <span class="pl-s1">texto</span> <span class="pl-c1">or</span> <span class="pl-c1">not</span> <span class="pl-s1">texto</span>.<span class="pl-c1">strip</span>():
        <span class="pl-k">return</span> <span class="pl-c1">None</span>

    <span class="pl-s1">texto_limpo</span> <span class="pl-c1">=</span> <span class="pl-s1">texto</span>.<span class="pl-c1">strip</span>()

    <span class="pl-k">if</span> <span class="pl-en">len</span>(<span class="pl-s1">texto_limpo</span>) <span class="pl-c1">&gt;</span> <span class="pl-s1">max_chars</span>:
        <span class="pl-k">raise</span> <span class="pl-en">ValidacaoError</span>(<span class="pl-s">f'Texto deve ter no máximo <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">max_chars</span><span class="pl-kos">}</span></span> caracteres'</span>)

    <span class="pl-k">return</span> <span class="pl-s1">texto_limpo</span>


<span class="pl-k">def</span> <span class="pl-en">validar_cpf</span>(<span class="pl-s1">cpf</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>]) <span class="pl-c1">-&gt;</span> <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>]:
    <span class="pl-s">"""</span>
<span class="pl-s">    Valida CPF brasileiro com dígitos verificadores</span>
<span class="pl-s"></span>
<span class="pl-s">    Args:</span>
<span class="pl-s">        cpf: CPF a ser validado (pode conter máscaras)</span>
<span class="pl-s"></span>
<span class="pl-s">    Returns:</span>
<span class="pl-s">        CPF limpo (apenas números) ou None se vazio</span>
<span class="pl-s"></span>
<span class="pl-s">    Raises:</span>
<span class="pl-s">        ValidacaoError: Se CPF for inválido</span>
<span class="pl-s">    """</span>
    <span class="pl-k">if</span> <span class="pl-c1">not</span> <span class="pl-s1">cpf</span>:
        <span class="pl-k">return</span> <span class="pl-c1">None</span>

    <span class="pl-c"># Remover caracteres especiais</span>
    <span class="pl-s1">cpf_limpo</span> <span class="pl-c1">=</span> <span class="pl-s1">re</span>.<span class="pl-c1">sub</span>(<span class="pl-s">r'[^0-9]'</span>, <span class="pl-s">''</span>, <span class="pl-s1">cpf</span>)

    <span class="pl-k">if</span> <span class="pl-en">len</span>(<span class="pl-s1">cpf_limpo</span>) <span class="pl-c1">!=</span> <span class="pl-c1">11</span>:
        <span class="pl-k">raise</span> <span class="pl-en">ValidacaoError</span>(<span class="pl-s">'CPF deve ter 11 dígitos'</span>)

    <span class="pl-c"># Verificar se todos os dígitos são iguais</span>
    <span class="pl-k">if</span> <span class="pl-s1">cpf_limpo</span> <span class="pl-c1">==</span> <span class="pl-s1">cpf_limpo</span>[<span class="pl-c1">0</span>] <span class="pl-c1">*</span> <span class="pl-c1">11</span>:
        <span class="pl-k">raise</span> <span class="pl-en">ValidacaoError</span>(<span class="pl-s">'CPF inválido'</span>)

    <span class="pl-c"># Validar dígito verificador</span>
    <span class="pl-k">def</span> <span class="pl-en">calcular_digito</span>(<span class="pl-s1">cpf_parcial</span>):
        <span class="pl-s1">soma</span> <span class="pl-c1">=</span> <span class="pl-en">sum</span>(<span class="pl-en">int</span>(<span class="pl-s1">cpf_parcial</span>[<span class="pl-s1">i</span>]) <span class="pl-c1">*</span> (<span class="pl-en">len</span>(<span class="pl-s1">cpf_parcial</span>) <span class="pl-c1">+</span> <span class="pl-c1">1</span> <span class="pl-c1">-</span> <span class="pl-s1">i</span>)
                   <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-en">len</span>(<span class="pl-s1">cpf_parcial</span>)))
        <span class="pl-s1">resto</span> <span class="pl-c1">=</span> <span class="pl-s1">soma</span> <span class="pl-c1">%</span> <span class="pl-c1">11</span>
        <span class="pl-k">return</span> <span class="pl-c1">0</span> <span class="pl-k">if</span> <span class="pl-s1">resto</span> <span class="pl-c1">&lt;</span> <span class="pl-c1">2</span> <span class="pl-k">else</span> <span class="pl-c1">11</span> <span class="pl-c1">-</span> <span class="pl-s1">resto</span>

    <span class="pl-k">if</span> <span class="pl-en">int</span>(<span class="pl-s1">cpf_limpo</span>[<span class="pl-c1">9</span>]) <span class="pl-c1">!=</span> <span class="pl-en">calcular_digito</span>(<span class="pl-s1">cpf_limpo</span>[:<span class="pl-c1">9</span>]):
        <span class="pl-k">raise</span> <span class="pl-en">ValidacaoError</span>(<span class="pl-s">'CPF inválido'</span>)

    <span class="pl-k">if</span> <span class="pl-en">int</span>(<span class="pl-s1">cpf_limpo</span>[<span class="pl-c1">10</span>]) <span class="pl-c1">!=</span> <span class="pl-en">calcular_digito</span>(<span class="pl-s1">cpf_limpo</span>[:<span class="pl-c1">10</span>]):
        <span class="pl-k">raise</span> <span class="pl-en">ValidacaoError</span>(<span class="pl-s">'CPF inválido'</span>)

    <span class="pl-k">return</span> <span class="pl-s1">cpf_limpo</span>


<span class="pl-k">def</span> <span class="pl-en">validar_telefone</span>(<span class="pl-s1">telefone</span>: <span class="pl-smi">str</span>) <span class="pl-c1">-&gt;</span> <span class="pl-smi">str</span>:
    <span class="pl-s">"""</span>
<span class="pl-s">    Valida telefone brasileiro (celular ou fixo)</span>
<span class="pl-s"></span>
<span class="pl-s">    Args:</span>
<span class="pl-s">        telefone: Telefone a ser validado</span>
<span class="pl-s"></span>
<span class="pl-s">    Returns:</span>
<span class="pl-s">        Telefone limpo (apenas números)</span>
<span class="pl-s"></span>
<span class="pl-s">    Raises:</span>
<span class="pl-s">        ValidacaoError: Se telefone for inválido</span>
<span class="pl-s">    """</span>
    <span class="pl-k">if</span> <span class="pl-c1">not</span> <span class="pl-s1">telefone</span>:
        <span class="pl-k">raise</span> <span class="pl-en">ValidacaoError</span>(<span class="pl-s">'Telefone é obrigatório'</span>)

    <span class="pl-c"># Remover caracteres especiais</span>
    <span class="pl-s1">telefone_limpo</span> <span class="pl-c1">=</span> <span class="pl-s1">re</span>.<span class="pl-c1">sub</span>(<span class="pl-s">r'[^0-9]'</span>, <span class="pl-s">''</span>, <span class="pl-s1">telefone</span>)

    <span class="pl-c"># Telefone deve ter 10 (fixo) ou 11 (celular) dígitos</span>
    <span class="pl-k">if</span> <span class="pl-en">len</span>(<span class="pl-s1">telefone_limpo</span>) <span class="pl-c1"><span class="pl-c1">not</span> <span class="pl-c1">in</span></span> [<span class="pl-c1">10</span>, <span class="pl-c1">11</span>]:
        <span class="pl-k">raise</span> <span class="pl-en">ValidacaoError</span>(<span class="pl-s">'Telefone deve ter 10 ou 11 dígitos'</span>)

    <span class="pl-c"># Validar DDD (11 a 99)</span>
    <span class="pl-s1">ddd</span> <span class="pl-c1">=</span> <span class="pl-en">int</span>(<span class="pl-s1">telefone_limpo</span>[:<span class="pl-c1">2</span>])
    <span class="pl-k">if</span> <span class="pl-s1">ddd</span> <span class="pl-c1">&lt;</span> <span class="pl-c1">11</span> <span class="pl-c1">or</span> <span class="pl-s1">ddd</span> <span class="pl-c1">&gt;</span> <span class="pl-c1">99</span>:
        <span class="pl-k">raise</span> <span class="pl-en">ValidacaoError</span>(<span class="pl-s">'DDD inválido'</span>)

    <span class="pl-k">return</span> <span class="pl-s1">telefone_limpo</span>


<span class="pl-k">def</span> <span class="pl-en">validar_valor_monetario</span>(
    <span class="pl-s1">valor</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">Decimal</span>],
    <span class="pl-s1">campo</span>: <span class="pl-smi">str</span> <span class="pl-c1">=</span> <span class="pl-s">"Valor"</span>,
    <span class="pl-s1">obrigatorio</span>: <span class="pl-smi">bool</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span>,
    <span class="pl-s1">min_valor</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">Decimal</span>] <span class="pl-c1">=</span> <span class="pl-c1">None</span>
) <span class="pl-c1">-&gt;</span> <span class="pl-v">Optional</span>[<span class="pl-smi">Decimal</span>]:
    <span class="pl-s">"""</span>
<span class="pl-s">    Valida valor monetário</span>
<span class="pl-s"></span>
<span class="pl-s">    Args:</span>
<span class="pl-s">        valor: Valor a ser validado</span>
<span class="pl-s">        campo: Nome do campo</span>
<span class="pl-s">        obrigatorio: Se o valor é obrigatório</span>
<span class="pl-s">        min_valor: Valor mínimo permitido</span>
<span class="pl-s"></span>
<span class="pl-s">    Returns:</span>
<span class="pl-s">        Valor validado</span>
<span class="pl-s"></span>
<span class="pl-s">    Raises:</span>
<span class="pl-s">        ValidacaoError: Se validação falhar</span>
<span class="pl-s">    """</span>
    <span class="pl-k">if</span> <span class="pl-s1">valor</span> <span class="pl-c1">is</span> <span class="pl-c1">None</span>:
        <span class="pl-k">if</span> <span class="pl-s1">obrigatorio</span>:
            <span class="pl-k">raise</span> <span class="pl-en">ValidacaoError</span>(<span class="pl-s">f'<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">campo</span><span class="pl-kos">}</span></span> é obrigatório'</span>)
        <span class="pl-k">return</span> <span class="pl-c1">None</span>

    <span class="pl-k">if</span> <span class="pl-c1">not</span> <span class="pl-en">isinstance</span>(<span class="pl-s1">valor</span>, <span class="pl-v">Decimal</span>):
        <span class="pl-k">try</span>:
            <span class="pl-s1">valor</span> <span class="pl-c1">=</span> <span class="pl-en">Decimal</span>(<span class="pl-en">str</span>(<span class="pl-s1">valor</span>))
        <span class="pl-k">except</span>:
            <span class="pl-k">raise</span> <span class="pl-en">ValidacaoError</span>(<span class="pl-s">f'<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">campo</span><span class="pl-kos">}</span></span> deve ser um valor numérico válido'</span>)

    <span class="pl-k">if</span> <span class="pl-s1">min_valor</span> <span class="pl-c1"><span class="pl-c1">is</span> <span class="pl-c1">not</span></span> <span class="pl-c1">None</span> <span class="pl-c1">and</span> <span class="pl-s1">valor</span> <span class="pl-c1">&lt;</span> <span class="pl-s1">min_valor</span>:
        <span class="pl-k">raise</span> <span class="pl-en">ValidacaoError</span>(<span class="pl-s">f'<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">campo</span><span class="pl-kos">}</span></span> deve ser maior ou igual a <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">min_valor</span><span class="pl-kos">}</span></span>'</span>)

    <span class="pl-k">return</span> <span class="pl-s1">valor</span>


<span class="pl-k">def</span> <span class="pl-en">validar_enum_valor</span>(<span class="pl-s1">valor</span>: <span class="pl-smi">any</span>, <span class="pl-s1">enum_class</span>, <span class="pl-s1">campo</span>: <span class="pl-smi">str</span> <span class="pl-c1">=</span> <span class="pl-s">"Campo"</span>):
    <span class="pl-s">"""</span>
<span class="pl-s">    Valida se valor está em um enum</span>
<span class="pl-s"></span>
<span class="pl-s">    Args:</span>
<span class="pl-s">        valor: Valor a ser validado</span>
<span class="pl-s">        enum_class: Classe do enum</span>
<span class="pl-s">        campo: Nome do campo</span>
<span class="pl-s"></span>
<span class="pl-s">    Returns:</span>
<span class="pl-s">        Valor do enum validado</span>
<span class="pl-s"></span>
<span class="pl-s">    Raises:</span>
<span class="pl-s">        ValidacaoError: Se valor não estiver no enum</span>
<span class="pl-s">    """</span>
    <span class="pl-k">if</span> <span class="pl-en">isinstance</span>(<span class="pl-s1">valor</span>, <span class="pl-s1">str</span>):
        <span class="pl-k">try</span>:
            <span class="pl-k">return</span> <span class="pl-en">enum_class</span>(<span class="pl-s1">valor</span>.<span class="pl-c1">upper</span>())
        <span class="pl-k">except</span> <span class="pl-v">ValueError</span>:
            <span class="pl-s1">valores_validos</span> <span class="pl-c1">=</span> [<span class="pl-s1">item</span>.<span class="pl-c1">value</span> <span class="pl-k">for</span> <span class="pl-s1">item</span> <span class="pl-c1">in</span> <span class="pl-s1">enum_class</span>]
            <span class="pl-k">raise</span> <span class="pl-en">ValidacaoError</span>(
                <span class="pl-s">f'<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">campo</span><span class="pl-kos">}</span></span> deve ser uma das opções: <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s">", "</span>.<span class="pl-c1">join</span>(<span class="pl-s1">valores_validos</span>)<span class="pl-kos">}</span></span>'</span>
            )

    <span class="pl-k">if</span> <span class="pl-s1">valor</span> <span class="pl-c1"><span class="pl-c1">not</span> <span class="pl-c1">in</span></span> <span class="pl-s1">enum_class</span>:
        <span class="pl-s1">valores_validos</span> <span class="pl-c1">=</span> [<span class="pl-s1">item</span>.<span class="pl-c1">value</span> <span class="pl-k">for</span> <span class="pl-s1">item</span> <span class="pl-c1">in</span> <span class="pl-s1">enum_class</span>]
        <span class="pl-k">raise</span> <span class="pl-en">ValidacaoError</span>(
            <span class="pl-s">f'<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">campo</span><span class="pl-kos">}</span></span> deve ser uma das opções: <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s">", "</span>.<span class="pl-c1">join</span>(<span class="pl-s1">valores_validos</span>)<span class="pl-kos">}</span></span>'</span>
        )

    <span class="pl-k">return</span> <span class="pl-s1">valor</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="import re
from typing import Optional
from decimal import Decimal

def validar_texto_obrigatorio(
    texto: str,
    campo: str = &quot;Campo&quot;,
    min_chars: int = 1,
    max_chars: int = 255
) -&gt; str:
    &quot;&quot;&quot;
    Valida texto obrigatório com limites de tamanho

    Args:
        texto: Texto a ser validado
        campo: Nome do campo (para mensagens de erro)
        min_chars: Tamanho mínimo
        max_chars: Tamanho máximo

    Returns:
        Texto validado e limpo

    Raises:
        ValidacaoError: Se validação falhar
    &quot;&quot;&quot;
    if not texto or not texto.strip():
        raise ValidacaoError(f&#39;{campo} é obrigatório&#39;)

    texto_limpo = texto.strip()

    if len(texto_limpo) &lt; min_chars:
        raise ValidacaoError(f&#39;{campo} deve ter pelo menos {min_chars} caracteres&#39;)

    if len(texto_limpo) &gt; max_chars:
        raise ValidacaoError(f&#39;{campo} deve ter no máximo {max_chars} caracteres&#39;)

    return texto_limpo


def validar_texto_opcional(
    texto: Optional[str],
    max_chars: int = 500
) -&gt; Optional[str]:
    &quot;&quot;&quot;
    Valida texto opcional

    Args:
        texto: Texto a ser validado (pode ser None)
        max_chars: Tamanho máximo

    Returns:
        Texto validado ou None

    Raises:
        ValidacaoError: Se texto exceder tamanho máximo
    &quot;&quot;&quot;
    if not texto or not texto.strip():
        return None

    texto_limpo = texto.strip()

    if len(texto_limpo) &gt; max_chars:
        raise ValidacaoError(f&#39;Texto deve ter no máximo {max_chars} caracteres&#39;)

    return texto_limpo


def validar_cpf(cpf: Optional[str]) -&gt; Optional[str]:
    &quot;&quot;&quot;
    Valida CPF brasileiro com dígitos verificadores

    Args:
        cpf: CPF a ser validado (pode conter máscaras)

    Returns:
        CPF limpo (apenas números) ou None se vazio

    Raises:
        ValidacaoError: Se CPF for inválido
    &quot;&quot;&quot;
    if not cpf:
        return None

    # Remover caracteres especiais
    cpf_limpo = re.sub(r&#39;[^0-9]&#39;, &#39;&#39;, cpf)

    if len(cpf_limpo) != 11:
        raise ValidacaoError(&#39;CPF deve ter 11 dígitos&#39;)

    # Verificar se todos os dígitos são iguais
    if cpf_limpo == cpf_limpo[0] * 11:
        raise ValidacaoError(&#39;CPF inválido&#39;)

    # Validar dígito verificador
    def calcular_digito(cpf_parcial):
        soma = sum(int(cpf_parcial[i]) * (len(cpf_parcial) + 1 - i)
                   for i in range(len(cpf_parcial)))
        resto = soma % 11
        return 0 if resto &lt; 2 else 11 - resto

    if int(cpf_limpo[9]) != calcular_digito(cpf_limpo[:9]):
        raise ValidacaoError(&#39;CPF inválido&#39;)

    if int(cpf_limpo[10]) != calcular_digito(cpf_limpo[:10]):
        raise ValidacaoError(&#39;CPF inválido&#39;)

    return cpf_limpo


def validar_telefone(telefone: str) -&gt; str:
    &quot;&quot;&quot;
    Valida telefone brasileiro (celular ou fixo)

    Args:
        telefone: Telefone a ser validado

    Returns:
        Telefone limpo (apenas números)

    Raises:
        ValidacaoError: Se telefone for inválido
    &quot;&quot;&quot;
    if not telefone:
        raise ValidacaoError(&#39;Telefone é obrigatório&#39;)

    # Remover caracteres especiais
    telefone_limpo = re.sub(r&#39;[^0-9]&#39;, &#39;&#39;, telefone)

    # Telefone deve ter 10 (fixo) ou 11 (celular) dígitos
    if len(telefone_limpo) not in [10, 11]:
        raise ValidacaoError(&#39;Telefone deve ter 10 ou 11 dígitos&#39;)

    # Validar DDD (11 a 99)
    ddd = int(telefone_limpo[:2])
    if ddd &lt; 11 or ddd &gt; 99:
        raise ValidacaoError(&#39;DDD inválido&#39;)

    return telefone_limpo


def validar_valor_monetario(
    valor: Optional[Decimal],
    campo: str = &quot;Valor&quot;,
    obrigatorio: bool = True,
    min_valor: Optional[Decimal] = None
) -&gt; Optional[Decimal]:
    &quot;&quot;&quot;
    Valida valor monetário

    Args:
        valor: Valor a ser validado
        campo: Nome do campo
        obrigatorio: Se o valor é obrigatório
        min_valor: Valor mínimo permitido

    Returns:
        Valor validado

    Raises:
        ValidacaoError: Se validação falhar
    &quot;&quot;&quot;
    if valor is None:
        if obrigatorio:
            raise ValidacaoError(f&#39;{campo} é obrigatório&#39;)
        return None

    if not isinstance(valor, Decimal):
        try:
            valor = Decimal(str(valor))
        except:
            raise ValidacaoError(f&#39;{campo} deve ser um valor numérico válido&#39;)

    if min_valor is not None and valor &lt; min_valor:
        raise ValidacaoError(f&#39;{campo} deve ser maior ou igual a {min_valor}&#39;)

    return valor


def validar_enum_valor(valor: any, enum_class, campo: str = &quot;Campo&quot;):
    &quot;&quot;&quot;
    Valida se valor está em um enum

    Args:
        valor: Valor a ser validado
        enum_class: Classe do enum
        campo: Nome do campo

    Returns:
        Valor do enum validado

    Raises:
        ValidacaoError: Se valor não estiver no enum
    &quot;&quot;&quot;
    if isinstance(valor, str):
        try:
            return enum_class(valor.upper())
        except ValueError:
            valores_validos = [item.value for item in enum_class]
            raise ValidacaoError(
                f&#39;{campo} deve ser uma das opções: {&quot;, &quot;.join(valores_validos)}&#39;
            )

    if valor not in enum_class:
        valores_validos = [item.value for item in enum_class]
        raise ValidacaoError(
            f&#39;{campo} deve ser uma das opções: {&quot;, &quot;.join(valores_validos)}&#39;
        )

    return valor" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><strong>PASSO 5: Criar ValidadorWrapper</strong></h3><a id="user-content-passo-5-criar-validadorwrapper" class="anchor" aria-label="Permalink: PASSO 5: Criar ValidadorWrapper" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#passo-5-criar-validadorwrapper"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong>Adicione ao final do arquivo <code>util/validacoes_dto.py</code>:</strong></p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">class</span> <span class="pl-v">ValidadorWrapper</span>:
    <span class="pl-s">"""</span>
<span class="pl-s">    Classe para facilitar o uso de validadores em field_validators.</span>
<span class="pl-s">    Reduz código repetitivo e padroniza tratamento de erros.</span>
<span class="pl-s">    """</span>

    <span class="pl-en">@<span class="pl-s1">staticmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">criar_validador</span>(<span class="pl-s1">funcao_validacao</span>, <span class="pl-s1">campo_nome</span>: <span class="pl-smi">str</span> <span class="pl-c1">=</span> <span class="pl-c1">None</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>):
        <span class="pl-s">"""</span>
<span class="pl-s">        Cria um validador pronto para usar com @field_validator.</span>
<span class="pl-s"></span>
<span class="pl-s">        Args:</span>
<span class="pl-s">            funcao_validacao: Função de validação a ser chamada</span>
<span class="pl-s">            campo_nome: Nome do campo para mensagens de erro</span>
<span class="pl-s">            **kwargs: Argumentos adicionais para a função</span>
<span class="pl-s"></span>
<span class="pl-s">        Returns:</span>
<span class="pl-s">            Função validador pronta para usar</span>
<span class="pl-s"></span>
<span class="pl-s">        Exemplo:</span>
<span class="pl-s">            validar_nome = ValidadorWrapper.criar_validador(</span>
<span class="pl-s">                validar_texto_obrigatorio, "Nome", min_chars=2, max_chars=100</span>
<span class="pl-s">            )</span>
<span class="pl-s">        """</span>
        <span class="pl-k">def</span> <span class="pl-en">validador</span>(<span class="pl-s1">valor</span>):
            <span class="pl-k">try</span>:
                <span class="pl-k">if</span> <span class="pl-s1">campo_nome</span>:
                    <span class="pl-k">return</span> <span class="pl-en">funcao_validacao</span>(<span class="pl-s1">valor</span>, <span class="pl-s1">campo_nome</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>)
                <span class="pl-k">else</span>:
                    <span class="pl-k">return</span> <span class="pl-en">funcao_validacao</span>(<span class="pl-s1">valor</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>)
            <span class="pl-k">except</span> <span class="pl-v">ValidacaoError</span> <span class="pl-k">as</span> <span class="pl-s1">e</span>:
                <span class="pl-k">raise</span> <span class="pl-en">ValueError</span>(<span class="pl-en">str</span>(<span class="pl-s1">e</span>))
        <span class="pl-k">return</span> <span class="pl-s1">validador</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="class ValidadorWrapper:
    &quot;&quot;&quot;
    Classe para facilitar o uso de validadores em field_validators.
    Reduz código repetitivo e padroniza tratamento de erros.
    &quot;&quot;&quot;

    @staticmethod
    def criar_validador(funcao_validacao, campo_nome: str = None, **kwargs):
        &quot;&quot;&quot;
        Cria um validador pronto para usar com @field_validator.

        Args:
            funcao_validacao: Função de validação a ser chamada
            campo_nome: Nome do campo para mensagens de erro
            **kwargs: Argumentos adicionais para a função

        Returns:
            Função validador pronta para usar

        Exemplo:
            validar_nome = ValidadorWrapper.criar_validador(
                validar_texto_obrigatorio, &quot;Nome&quot;, min_chars=2, max_chars=100
            )
        &quot;&quot;&quot;
        def validador(valor):
            try:
                if campo_nome:
                    return funcao_validacao(valor, campo_nome, **kwargs)
                else:
                    return funcao_validacao(valor, **kwargs)
            except ValidacaoError as e:
                raise ValueError(str(e))
        return validador" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><strong>PASSO 6: Criar BaseDTO</strong></h3><a id="user-content-passo-6-criar-basedto" class="anchor" aria-label="Permalink: PASSO 6: Criar BaseDTO" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#passo-6-criar-basedto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong>Arquivo: <code>dtos/base_dto.py</code></strong></p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-s">"""</span>
<span class="pl-s">Classe base para todos os DTOs do sistema.</span>
<span class="pl-s">Fornece configurações padrão e métodos de validação comuns.</span>
<span class="pl-s">"""</span>

<span class="pl-k">from</span> <span class="pl-s1">pydantic</span> <span class="pl-k">import</span> <span class="pl-v">BaseModel</span>, <span class="pl-v">ConfigDict</span>
<span class="pl-k">from</span> <span class="pl-s1">typing</span> <span class="pl-k">import</span> <span class="pl-v">Dict</span>, <span class="pl-v">Any</span>
<span class="pl-k">from</span> <span class="pl-s1">util</span>.<span class="pl-s1">validacoes_dto</span> <span class="pl-k">import</span> <span class="pl-v">ValidacaoError</span>


<span class="pl-k">class</span> <span class="pl-v">BaseDTO</span>(<span class="pl-v">BaseModel</span>):
    <span class="pl-s">"""</span>
<span class="pl-s">    Classe base para todos os DTOs do sistema.</span>
<span class="pl-s">    Fornece configurações padrão e métodos de validação comuns.</span>
<span class="pl-s"></span>
<span class="pl-s">    Esta classe implementa:</span>
<span class="pl-s">    - Configurações padrão do Pydantic</span>
<span class="pl-s">    - Wrapper para tratamento de erros de validação</span>
<span class="pl-s">    - Métodos auxiliares para conversão de dados</span>
<span class="pl-s">    """</span>

    <span class="pl-s1">model_config</span> <span class="pl-c1">=</span> <span class="pl-en">ConfigDict</span>(
        <span class="pl-c"># Remover espaços em branco automaticamente</span>
        <span class="pl-s1">str_strip_whitespace</span><span class="pl-c1">=</span><span class="pl-c1">True</span>,
        <span class="pl-c"># Validar na atribuição também (não só na criação)</span>
        <span class="pl-s1">validate_assignment</span><span class="pl-c1">=</span><span class="pl-c1">True</span>,
        <span class="pl-c"># Usar valores dos enums ao invés dos objetos</span>
        <span class="pl-s1">use_enum_values</span><span class="pl-c1">=</span><span class="pl-c1">True</span>,
        <span class="pl-c"># Permitir population by name (útil para formulários HTML)</span>
        <span class="pl-s1">populate_by_name</span><span class="pl-c1">=</span><span class="pl-c1">True</span>,
        <span class="pl-c"># Validar valores padrão também</span>
        <span class="pl-s1">validate_default</span><span class="pl-c1">=</span><span class="pl-c1">True</span>
    )

    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">criar_exemplo_json</span>(<span class="pl-s1">cls</span>, <span class="pl-c1">**</span><span class="pl-s1">overrides</span>) <span class="pl-c1">-&gt;</span> <span class="pl-v">Dict</span>[<span class="pl-smi">str</span>, <span class="pl-smi">Any</span>]:
        <span class="pl-s">"""</span>
<span class="pl-s">        Cria um exemplo JSON para documentação da API.</span>
<span class="pl-s">        Pode ser sobrescrito nas classes filhas.</span>
<span class="pl-s"></span>
<span class="pl-s">        Args:</span>
<span class="pl-s">            **overrides: Valores específicos para sobrescrever no exemplo</span>
<span class="pl-s"></span>
<span class="pl-s">        Returns:</span>
<span class="pl-s">            Dict com exemplo de dados para este DTO</span>
<span class="pl-s">        """</span>
        <span class="pl-k">return</span> {<span class="pl-s">"exemplo"</span>: <span class="pl-s">"Sobrescrever na classe filha"</span>, <span class="pl-c1">**</span><span class="pl-s1">overrides</span>}

    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">validar_campo_wrapper</span>(<span class="pl-s1">cls</span>, <span class="pl-s1">validador_func</span>, <span class="pl-s1">campo_nome</span>: <span class="pl-smi">str</span> <span class="pl-c1">=</span> <span class="pl-s">""</span>):
        <span class="pl-s">"""</span>
<span class="pl-s">        Wrapper para padronizar o tratamento de erros de validação.</span>
<span class="pl-s">        Evita repetir try/except em cada field_validator.</span>
<span class="pl-s"></span>
<span class="pl-s">        Args:</span>
<span class="pl-s">            validador_func: Função de validação a ser envolvida</span>
<span class="pl-s">            campo_nome: Nome do campo para mensagens de erro</span>
<span class="pl-s"></span>
<span class="pl-s">        Returns:</span>
<span class="pl-s">            Função wrapper que trata os erros automaticamente</span>
<span class="pl-s">        """</span>
        <span class="pl-k">def</span> <span class="pl-en">wrapper</span>(<span class="pl-s1">valor</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>):
            <span class="pl-k">try</span>:
                <span class="pl-k">if</span> <span class="pl-s1">campo_nome</span>:
                    <span class="pl-k">return</span> <span class="pl-en">validador_func</span>(<span class="pl-s1">valor</span>, <span class="pl-s1">campo_nome</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>)
                <span class="pl-k">else</span>:
                    <span class="pl-k">return</span> <span class="pl-en">validador_func</span>(<span class="pl-s1">valor</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>)
            <span class="pl-k">except</span> <span class="pl-v">ValidacaoError</span> <span class="pl-k">as</span> <span class="pl-s1">e</span>:
                <span class="pl-k">raise</span> <span class="pl-en">ValueError</span>(<span class="pl-en">str</span>(<span class="pl-s1">e</span>))
        <span class="pl-k">return</span> <span class="pl-s1">wrapper</span>

    <span class="pl-k">def</span> <span class="pl-en">to_dict</span>(<span class="pl-s1">self</span>) <span class="pl-c1">-&gt;</span> <span class="pl-smi">dict</span>:
        <span class="pl-s">"""</span>
<span class="pl-s">        Converte DTO para dicionário simples.</span>
<span class="pl-s">        Remove campos None para limpar o retorno.</span>
<span class="pl-s"></span>
<span class="pl-s">        Returns:</span>
<span class="pl-s">            Dicionário com os dados do DTO</span>
<span class="pl-s">        """</span>
        <span class="pl-k">return</span> <span class="pl-s1">self</span>.<span class="pl-c1">model_dump</span>(<span class="pl-s1">exclude_none</span><span class="pl-c1">=</span><span class="pl-c1">True</span>)

    <span class="pl-k">def</span> <span class="pl-en">to_json</span>(<span class="pl-s1">self</span>) <span class="pl-c1">-&gt;</span> <span class="pl-smi">str</span>:
        <span class="pl-s">"""</span>
<span class="pl-s">        Converte DTO para JSON.</span>
<span class="pl-s">        Remove campos None para limpar o retorno.</span>
<span class="pl-s"></span>
<span class="pl-s">        Returns:</span>
<span class="pl-s">            String JSON com os dados do DTO</span>
<span class="pl-s">        """</span>
        <span class="pl-k">return</span> <span class="pl-s1">self</span>.<span class="pl-c1">model_dump_json</span>(<span class="pl-s1">exclude_none</span><span class="pl-c1">=</span><span class="pl-c1">True</span>)

    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">from_dict</span>(<span class="pl-s1">cls</span>, <span class="pl-s1">data</span>: <span class="pl-smi">dict</span>):
        <span class="pl-s">"""</span>
<span class="pl-s">        Cria DTO a partir de dicionário.</span>
<span class="pl-s"></span>
<span class="pl-s">        Args:</span>
<span class="pl-s">            data: Dicionário com os dados</span>
<span class="pl-s"></span>
<span class="pl-s">        Returns:</span>
<span class="pl-s">            Instância do DTO</span>
<span class="pl-s">        """</span>
        <span class="pl-k">return</span> <span class="pl-en">cls</span>(<span class="pl-c1">**</span><span class="pl-s1">data</span>)

    <span class="pl-k">def</span> <span class="pl-en">__str__</span>(<span class="pl-s1">self</span>) <span class="pl-c1">-&gt;</span> <span class="pl-smi">str</span>:
        <span class="pl-s">"""Representação string melhorada do DTO"""</span>
        <span class="pl-s1">campos</span> <span class="pl-c1">=</span> <span class="pl-s">', '</span>.<span class="pl-c1">join</span>([<span class="pl-s">f"<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">k</span><span class="pl-kos">}</span></span>=<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">v</span><span class="pl-kos">}</span></span>"</span> <span class="pl-k">for</span> <span class="pl-s1">k</span>, <span class="pl-s1">v</span> <span class="pl-c1">in</span> <span class="pl-s1">self</span>.<span class="pl-c1">to_dict</span>().<span class="pl-c1">items</span>()])
        <span class="pl-k">return</span> <span class="pl-s">f"<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">self</span>.<span class="pl-c1">__class__</span>.<span class="pl-c1">__name__</span><span class="pl-kos">}</span></span>(<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">campos</span><span class="pl-kos">}</span></span>)"</span>

    <span class="pl-k">def</span> <span class="pl-en">__repr__</span>(<span class="pl-s1">self</span>) <span class="pl-c1">-&gt;</span> <span class="pl-smi">str</span>:
        <span class="pl-s">"""Representação técnica do DTO"""</span>
        <span class="pl-k">return</span> <span class="pl-s1">self</span>.<span class="pl-c1">__str__</span>()</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="&quot;&quot;&quot;
Classe base para todos os DTOs do sistema.
Fornece configurações padrão e métodos de validação comuns.
&quot;&quot;&quot;

from pydantic import BaseModel, ConfigDict
from typing import Dict, Any
from util.validacoes_dto import ValidacaoError


class BaseDTO(BaseModel):
    &quot;&quot;&quot;
    Classe base para todos os DTOs do sistema.
    Fornece configurações padrão e métodos de validação comuns.

    Esta classe implementa:
    - Configurações padrão do Pydantic
    - Wrapper para tratamento de erros de validação
    - Métodos auxiliares para conversão de dados
    &quot;&quot;&quot;

    model_config = ConfigDict(
        # Remover espaços em branco automaticamente
        str_strip_whitespace=True,
        # Validar na atribuição também (não só na criação)
        validate_assignment=True,
        # Usar valores dos enums ao invés dos objetos
        use_enum_values=True,
        # Permitir population by name (útil para formulários HTML)
        populate_by_name=True,
        # Validar valores padrão também
        validate_default=True
    )

    @classmethod
    def criar_exemplo_json(cls, **overrides) -&gt; Dict[str, Any]:
        &quot;&quot;&quot;
        Cria um exemplo JSON para documentação da API.
        Pode ser sobrescrito nas classes filhas.

        Args:
            **overrides: Valores específicos para sobrescrever no exemplo

        Returns:
            Dict com exemplo de dados para este DTO
        &quot;&quot;&quot;
        return {&quot;exemplo&quot;: &quot;Sobrescrever na classe filha&quot;, **overrides}

    @classmethod
    def validar_campo_wrapper(cls, validador_func, campo_nome: str = &quot;&quot;):
        &quot;&quot;&quot;
        Wrapper para padronizar o tratamento de erros de validação.
        Evita repetir try/except em cada field_validator.

        Args:
            validador_func: Função de validação a ser envolvida
            campo_nome: Nome do campo para mensagens de erro

        Returns:
            Função wrapper que trata os erros automaticamente
        &quot;&quot;&quot;
        def wrapper(valor, **kwargs):
            try:
                if campo_nome:
                    return validador_func(valor, campo_nome, **kwargs)
                else:
                    return validador_func(valor, **kwargs)
            except ValidacaoError as e:
                raise ValueError(str(e))
        return wrapper

    def to_dict(self) -&gt; dict:
        &quot;&quot;&quot;
        Converte DTO para dicionário simples.
        Remove campos None para limpar o retorno.

        Returns:
            Dicionário com os dados do DTO
        &quot;&quot;&quot;
        return self.model_dump(exclude_none=True)

    def to_json(self) -&gt; str:
        &quot;&quot;&quot;
        Converte DTO para JSON.
        Remove campos None para limpar o retorno.

        Returns:
            String JSON com os dados do DTO
        &quot;&quot;&quot;
        return self.model_dump_json(exclude_none=True)

    @classmethod
    def from_dict(cls, data: dict):
        &quot;&quot;&quot;
        Cria DTO a partir de dicionário.

        Args:
            data: Dicionário com os dados

        Returns:
            Instância do DTO
        &quot;&quot;&quot;
        return cls(**data)

    def __str__(self) -&gt; str:
        &quot;&quot;&quot;Representação string melhorada do DTO&quot;&quot;&quot;
        campos = &#39;, &#39;.join([f&quot;{k}={v}&quot; for k, v in self.to_dict().items()])
        return f&quot;{self.__class__.__name__}({campos})&quot;

    def __repr__(self) -&gt; str:
        &quot;&quot;&quot;Representação técnica do DTO&quot;&quot;&quot;
        return self.__str__()" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><strong>PASSO 7: Criar Primeiro DTO por Domínio</strong></h3><a id="user-content-passo-7-criar-primeiro-dto-por-domínio" class="anchor" aria-label="Permalink: PASSO 7: Criar Primeiro DTO por Domínio" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#passo-7-criar-primeiro-dto-por-dom%C3%ADnio"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong>Arquivo: <code>dtos/usuario_dtos.py</code></strong></p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-s">"""</span>
<span class="pl-s">DTOs relacionados a usuários.</span>
<span class="pl-s">Agrupa todas as validações e estruturas de dados para operações com usuários.</span>
<span class="pl-s">"""</span>

<span class="pl-k">from</span> <span class="pl-s1">pydantic</span> <span class="pl-k">import</span> <span class="pl-v">EmailStr</span>, <span class="pl-v">Field</span>, <span class="pl-s1">field_validator</span>
<span class="pl-k">from</span> <span class="pl-s1">typing</span> <span class="pl-k">import</span> <span class="pl-v">Optional</span>
<span class="pl-k">from</span> .<span class="pl-s1">base_dto</span> <span class="pl-k">import</span> <span class="pl-v">BaseDTO</span>
<span class="pl-k">from</span> <span class="pl-s1">util</span>.<span class="pl-s1">validacoes_dto</span> <span class="pl-k">import</span> (
    <span class="pl-s1">validar_texto_obrigatorio</span>, <span class="pl-s1">validar_cpf</span>, <span class="pl-s1">validar_telefone</span>
)


<span class="pl-k">class</span> <span class="pl-v">CriarUsuarioDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s">"""</span>
<span class="pl-s">    DTO para criação de novo usuário.</span>
<span class="pl-s">    Usado em formulários de registro.</span>
<span class="pl-s">    """</span>

    <span class="pl-s1">nome</span>: <span class="pl-smi">str</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(
        ...,
        <span class="pl-s1">min_length</span><span class="pl-c1">=</span><span class="pl-c1">2</span>,
        <span class="pl-s1">max_length</span><span class="pl-c1">=</span><span class="pl-c1">100</span>,
        <span class="pl-s1">description</span><span class="pl-c1">=</span><span class="pl-s">"Nome completo do usuário"</span>
    )
    <span class="pl-s1">email</span>: <span class="pl-smi">EmailStr</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(
        ...,
        <span class="pl-s1">description</span><span class="pl-c1">=</span><span class="pl-s">"E-mail válido do usuário"</span>
    )
    <span class="pl-s1">telefone</span>: <span class="pl-smi">str</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(
        ...,
        <span class="pl-s1">min_length</span><span class="pl-c1">=</span><span class="pl-c1">10</span>,
        <span class="pl-s1">description</span><span class="pl-c1">=</span><span class="pl-s">"Telefone com DDD"</span>
    )
    <span class="pl-s1">cpf</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>] <span class="pl-c1">=</span> <span class="pl-en">Field</span>(
        <span class="pl-c1">None</span>,
        <span class="pl-s1">description</span><span class="pl-c1">=</span><span class="pl-s">"CPF (opcional)"</span>
    )

    <span class="pl-en">@<span class="pl-en">field_validator</span>(<span class="pl-s">'nome'</span>)</span>
    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">validar_nome</span>(<span class="pl-s1">cls</span>, <span class="pl-s1">v</span>: <span class="pl-smi">str</span>) <span class="pl-c1">-&gt;</span> <span class="pl-smi">str</span>:
        <span class="pl-s1">validador</span> <span class="pl-c1">=</span> <span class="pl-s1">cls</span>.<span class="pl-c1">validar_campo_wrapper</span>(
            <span class="pl-k">lambda</span> <span class="pl-s1">valor</span>, <span class="pl-s1">campo</span>: <span class="pl-en">validar_texto_obrigatorio</span>(
                <span class="pl-s1">valor</span>, <span class="pl-s1">campo</span>, <span class="pl-s1">min_chars</span><span class="pl-c1">=</span><span class="pl-c1">2</span>, <span class="pl-s1">max_chars</span><span class="pl-c1">=</span><span class="pl-c1">100</span>
            ),
            <span class="pl-s">"Nome"</span>
        )
        <span class="pl-k">return</span> <span class="pl-en">validador</span>(<span class="pl-s1">v</span>)

    <span class="pl-en">@<span class="pl-en">field_validator</span>(<span class="pl-s">'cpf'</span>)</span>
    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">validar_cpf_campo</span>(<span class="pl-s1">cls</span>, <span class="pl-s1">v</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>]) <span class="pl-c1">-&gt;</span> <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>]:
        <span class="pl-k">if</span> <span class="pl-c1">not</span> <span class="pl-s1">v</span>:
            <span class="pl-k">return</span> <span class="pl-s1">v</span>
        <span class="pl-s1">validador</span> <span class="pl-c1">=</span> <span class="pl-s1">cls</span>.<span class="pl-c1">validar_campo_wrapper</span>(
            <span class="pl-k">lambda</span> <span class="pl-s1">valor</span>, <span class="pl-s1">campo</span>: <span class="pl-en">validar_cpf</span>(<span class="pl-s1">valor</span>),
            <span class="pl-s">"CPF"</span>
        )
        <span class="pl-k">return</span> <span class="pl-en">validador</span>(<span class="pl-s1">v</span>)

    <span class="pl-en">@<span class="pl-en">field_validator</span>(<span class="pl-s">'telefone'</span>)</span>
    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">validar_telefone_campo</span>(<span class="pl-s1">cls</span>, <span class="pl-s1">v</span>: <span class="pl-smi">str</span>) <span class="pl-c1">-&gt;</span> <span class="pl-smi">str</span>:
        <span class="pl-s1">validador</span> <span class="pl-c1">=</span> <span class="pl-s1">cls</span>.<span class="pl-c1">validar_campo_wrapper</span>(
            <span class="pl-k">lambda</span> <span class="pl-s1">valor</span>, <span class="pl-s1">campo</span>: <span class="pl-en">validar_telefone</span>(<span class="pl-s1">valor</span>),
            <span class="pl-s">"Telefone"</span>
        )
        <span class="pl-k">return</span> <span class="pl-en">validador</span>(<span class="pl-s1">v</span>)

    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">criar_exemplo_json</span>(<span class="pl-s1">cls</span>, <span class="pl-c1">**</span><span class="pl-s1">overrides</span>) <span class="pl-c1">-&gt;</span> <span class="pl-smi">dict</span>:
        <span class="pl-s">"""Exemplo de dados para documentação da API"""</span>
        <span class="pl-s1">exemplo</span> <span class="pl-c1">=</span> {
            <span class="pl-s">"nome"</span>: <span class="pl-s">"João Silva"</span>,
            <span class="pl-s">"email"</span>: <span class="pl-s">"joao.silva@email.com"</span>,
            <span class="pl-s">"telefone"</span>: <span class="pl-s">"(11) 99999-9999"</span>,
            <span class="pl-s">"cpf"</span>: <span class="pl-s">"123.456.789-01"</span>
        }
        <span class="pl-s1">exemplo</span>.<span class="pl-c1">update</span>(<span class="pl-s1">overrides</span>)
        <span class="pl-k">return</span> <span class="pl-s1">exemplo</span>


<span class="pl-k">class</span> <span class="pl-v">AtualizarUsuarioDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s">"""</span>
<span class="pl-s">    DTO para atualização de dados do usuário.</span>
<span class="pl-s">    Campos opcionais para atualização parcial.</span>
<span class="pl-s">    """</span>

    <span class="pl-s1">nome</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>] <span class="pl-c1">=</span> <span class="pl-en">Field</span>(
        <span class="pl-c1">None</span>,
        <span class="pl-s1">min_length</span><span class="pl-c1">=</span><span class="pl-c1">2</span>,
        <span class="pl-s1">max_length</span><span class="pl-c1">=</span><span class="pl-c1">100</span>,
        <span class="pl-s1">description</span><span class="pl-c1">=</span><span class="pl-s">"Nome completo"</span>
    )
    <span class="pl-s1">telefone</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>] <span class="pl-c1">=</span> <span class="pl-en">Field</span>(
        <span class="pl-c1">None</span>,
        <span class="pl-s1">description</span><span class="pl-c1">=</span><span class="pl-s">"Telefone"</span>
    )

    <span class="pl-en">@<span class="pl-en">field_validator</span>(<span class="pl-s">'nome'</span>)</span>
    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">validar_nome</span>(<span class="pl-s1">cls</span>, <span class="pl-s1">v</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>]) <span class="pl-c1">-&gt;</span> <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>]:
        <span class="pl-k">if</span> <span class="pl-c1">not</span> <span class="pl-s1">v</span>:
            <span class="pl-k">return</span> <span class="pl-s1">v</span>
        <span class="pl-s1">validador</span> <span class="pl-c1">=</span> <span class="pl-s1">cls</span>.<span class="pl-c1">validar_campo_wrapper</span>(
            <span class="pl-k">lambda</span> <span class="pl-s1">valor</span>, <span class="pl-s1">campo</span>: <span class="pl-en">validar_texto_obrigatorio</span>(
                <span class="pl-s1">valor</span>, <span class="pl-s1">campo</span>, <span class="pl-s1">min_chars</span><span class="pl-c1">=</span><span class="pl-c1">2</span>, <span class="pl-s1">max_chars</span><span class="pl-c1">=</span><span class="pl-c1">100</span>
            ),
            <span class="pl-s">"Nome"</span>
        )
        <span class="pl-k">return</span> <span class="pl-en">validador</span>(<span class="pl-s1">v</span>)

    <span class="pl-en">@<span class="pl-en">field_validator</span>(<span class="pl-s">'telefone'</span>)</span>
    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">validar_telefone_campo</span>(<span class="pl-s1">cls</span>, <span class="pl-s1">v</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>]) <span class="pl-c1">-&gt;</span> <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>]:
        <span class="pl-k">if</span> <span class="pl-c1">not</span> <span class="pl-s1">v</span>:
            <span class="pl-k">return</span> <span class="pl-s1">v</span>
        <span class="pl-s1">validador</span> <span class="pl-c1">=</span> <span class="pl-s1">cls</span>.<span class="pl-c1">validar_campo_wrapper</span>(
            <span class="pl-k">lambda</span> <span class="pl-s1">valor</span>, <span class="pl-s1">campo</span>: <span class="pl-en">validar_telefone</span>(<span class="pl-s1">valor</span>),
            <span class="pl-s">"Telefone"</span>
        )
        <span class="pl-k">return</span> <span class="pl-en">validador</span>(<span class="pl-s1">v</span>)


<span class="pl-c"># Configurar exemplos JSON nos model_config</span>
<span class="pl-v">CriarUsuarioDTO</span>.<span class="pl-c1">model_config</span>.<span class="pl-c1">update</span>({
    <span class="pl-s">"json_schema_extra"</span>: {
        <span class="pl-s">"example"</span>: <span class="pl-v">CriarUsuarioDTO</span>.<span class="pl-c1">criar_exemplo_json</span>()
    }
})</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="&quot;&quot;&quot;
DTOs relacionados a usuários.
Agrupa todas as validações e estruturas de dados para operações com usuários.
&quot;&quot;&quot;

from pydantic import EmailStr, Field, field_validator
from typing import Optional
from .base_dto import BaseDTO
from util.validacoes_dto import (
    validar_texto_obrigatorio, validar_cpf, validar_telefone
)


class CriarUsuarioDTO(BaseDTO):
    &quot;&quot;&quot;
    DTO para criação de novo usuário.
    Usado em formulários de registro.
    &quot;&quot;&quot;

    nome: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description=&quot;Nome completo do usuário&quot;
    )
    email: EmailStr = Field(
        ...,
        description=&quot;E-mail válido do usuário&quot;
    )
    telefone: str = Field(
        ...,
        min_length=10,
        description=&quot;Telefone com DDD&quot;
    )
    cpf: Optional[str] = Field(
        None,
        description=&quot;CPF (opcional)&quot;
    )

    @field_validator(&#39;nome&#39;)
    @classmethod
    def validar_nome(cls, v: str) -&gt; str:
        validador = cls.validar_campo_wrapper(
            lambda valor, campo: validar_texto_obrigatorio(
                valor, campo, min_chars=2, max_chars=100
            ),
            &quot;Nome&quot;
        )
        return validador(v)

    @field_validator(&#39;cpf&#39;)
    @classmethod
    def validar_cpf_campo(cls, v: Optional[str]) -&gt; Optional[str]:
        if not v:
            return v
        validador = cls.validar_campo_wrapper(
            lambda valor, campo: validar_cpf(valor),
            &quot;CPF&quot;
        )
        return validador(v)

    @field_validator(&#39;telefone&#39;)
    @classmethod
    def validar_telefone_campo(cls, v: str) -&gt; str:
        validador = cls.validar_campo_wrapper(
            lambda valor, campo: validar_telefone(valor),
            &quot;Telefone&quot;
        )
        return validador(v)

    @classmethod
    def criar_exemplo_json(cls, **overrides) -&gt; dict:
        &quot;&quot;&quot;Exemplo de dados para documentação da API&quot;&quot;&quot;
        exemplo = {
            &quot;nome&quot;: &quot;João Silva&quot;,
            &quot;email&quot;: &quot;joao.silva@email.com&quot;,
            &quot;telefone&quot;: &quot;(11) 99999-9999&quot;,
            &quot;cpf&quot;: &quot;123.456.789-01&quot;
        }
        exemplo.update(overrides)
        return exemplo


class AtualizarUsuarioDTO(BaseDTO):
    &quot;&quot;&quot;
    DTO para atualização de dados do usuário.
    Campos opcionais para atualização parcial.
    &quot;&quot;&quot;

    nome: Optional[str] = Field(
        None,
        min_length=2,
        max_length=100,
        description=&quot;Nome completo&quot;
    )
    telefone: Optional[str] = Field(
        None,
        description=&quot;Telefone&quot;
    )

    @field_validator(&#39;nome&#39;)
    @classmethod
    def validar_nome(cls, v: Optional[str]) -&gt; Optional[str]:
        if not v:
            return v
        validador = cls.validar_campo_wrapper(
            lambda valor, campo: validar_texto_obrigatorio(
                valor, campo, min_chars=2, max_chars=100
            ),
            &quot;Nome&quot;
        )
        return validador(v)

    @field_validator(&#39;telefone&#39;)
    @classmethod
    def validar_telefone_campo(cls, v: Optional[str]) -&gt; Optional[str]:
        if not v:
            return v
        validador = cls.validar_campo_wrapper(
            lambda valor, campo: validar_telefone(valor),
            &quot;Telefone&quot;
        )
        return validador(v)


# Configurar exemplos JSON nos model_config
CriarUsuarioDTO.model_config.update({
    &quot;json_schema_extra&quot;: {
        &quot;example&quot;: CriarUsuarioDTO.criar_exemplo_json()
    }
})" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><strong>PASSO 8: Configurar Imports Facilitados</strong></h3><a id="user-content-passo-8-configurar-imports-facilitados" class="anchor" aria-label="Permalink: PASSO 8: Configurar Imports Facilitados" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#passo-8-configurar-imports-facilitados"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong>Arquivo: <code>dtos/__init__.py</code></strong></p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-s">"""</span>
<span class="pl-s">Pacote de DTOs do sistema.</span>
<span class="pl-s"></span>
<span class="pl-s">Este módulo centraliza todos os DTOs (Data Transfer Objects) organizados por funcionalidade:</span>
<span class="pl-s">- BaseDTO: Classe base com configurações comuns</span>
<span class="pl-s">- usuario_dtos: DTOs relacionados a usuários</span>
<span class="pl-s"></span>
<span class="pl-s">Imports facilitados para os DTOs mais comuns:</span>
<span class="pl-s">"""</span>

<span class="pl-c"># Base</span>
<span class="pl-k">from</span> .<span class="pl-s1">base_dto</span> <span class="pl-k">import</span> <span class="pl-v">BaseDTO</span>

<span class="pl-c"># Usuário</span>
<span class="pl-k">from</span> .<span class="pl-s1">usuario_dtos</span> <span class="pl-k">import</span> (
    <span class="pl-v">CriarUsuarioDTO</span>,
    <span class="pl-v">AtualizarUsuarioDTO</span>
)

<span class="pl-s1">__all__</span> <span class="pl-c1">=</span> [
    <span class="pl-c"># Base</span>
    <span class="pl-s">'BaseDTO'</span>,

    <span class="pl-c"># Usuário</span>
    <span class="pl-s">'CriarUsuarioDTO'</span>,
    <span class="pl-s">'AtualizarUsuarioDTO'</span>,
]</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="&quot;&quot;&quot;
Pacote de DTOs do sistema.

Este módulo centraliza todos os DTOs (Data Transfer Objects) organizados por funcionalidade:
- BaseDTO: Classe base com configurações comuns
- usuario_dtos: DTOs relacionados a usuários

Imports facilitados para os DTOs mais comuns:
&quot;&quot;&quot;

# Base
from .base_dto import BaseDTO

# Usuário
from .usuario_dtos import (
    CriarUsuarioDTO,
    AtualizarUsuarioDTO
)

__all__ = [
    # Base
    &#39;BaseDTO&#39;,

    # Usuário
    &#39;CriarUsuarioDTO&#39;,
    &#39;AtualizarUsuarioDTO&#39;,
]" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><strong>PASSO 9: Usar DTOs em Rotas/Controllers</strong></h3><a id="user-content-passo-9-usar-dtos-em-rotascontrollers" class="anchor" aria-label="Permalink: PASSO 9: Usar DTOs em Rotas/Controllers" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#passo-9-usar-dtos-em-rotascontrollers"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong>Exemplo com FastAPI:</strong></p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">from</span> <span class="pl-s1">fastapi</span> <span class="pl-k">import</span> <span class="pl-v">APIRouter</span>, <span class="pl-v">HTTPException</span>
<span class="pl-k">from</span> <span class="pl-s1">dtos</span> <span class="pl-k">import</span> <span class="pl-v">CriarUsuarioDTO</span>, <span class="pl-v">AtualizarUsuarioDTO</span>
<span class="pl-k">from</span> <span class="pl-s1">pydantic</span> <span class="pl-k">import</span> <span class="pl-v">ValidationError</span>

<span class="pl-s1">router</span> <span class="pl-c1">=</span> <span class="pl-en">APIRouter</span>()

<span class="pl-en">@<span class="pl-s1">router</span>.<span class="pl-c1">post</span>(<span class="pl-s">"/usuarios"</span>)</span>
<span class="pl-k">def</span> <span class="pl-en">criar_usuario</span>(<span class="pl-s1">usuario_dto</span>: <span class="pl-smi">CriarUsuarioDTO</span>):
    <span class="pl-s">"""</span>
<span class="pl-s">    Cria um novo usuário.</span>
<span class="pl-s"></span>
<span class="pl-s">    A validação é automática! Se os dados forem inválidos,</span>
<span class="pl-s">    FastAPI retorna 422 automaticamente.</span>
<span class="pl-s">    """</span>
    <span class="pl-k">try</span>:
        <span class="pl-c"># Converter DTO para dict</span>
        <span class="pl-s1">dados</span> <span class="pl-c1">=</span> <span class="pl-s1">usuario_dto</span>.<span class="pl-c1">to_dict</span>()

        <span class="pl-c"># Salvar no banco de dados</span>
        <span class="pl-c"># usuario_service.criar(dados)</span>

        <span class="pl-k">return</span> {<span class="pl-s">"mensagem"</span>: <span class="pl-s">"Usuário criado com sucesso"</span>, <span class="pl-s">"dados"</span>: <span class="pl-s1">dados</span>}

    <span class="pl-k">except</span> <span class="pl-v">Exception</span> <span class="pl-k">as</span> <span class="pl-s1">e</span>:
        <span class="pl-k">raise</span> <span class="pl-en">HTTPException</span>(<span class="pl-s1">status_code</span><span class="pl-c1">=</span><span class="pl-c1">400</span>, <span class="pl-s1">detail</span><span class="pl-c1">=</span><span class="pl-en">str</span>(<span class="pl-s1">e</span>))


<span class="pl-en">@<span class="pl-s1">router</span>.<span class="pl-c1">put</span>(<span class="pl-s">"/usuarios/{id}"</span>)</span>
<span class="pl-k">def</span> <span class="pl-en">atualizar_usuario</span>(<span class="pl-s1">id</span>: <span class="pl-smi">int</span>, <span class="pl-s1">usuario_dto</span>: <span class="pl-smi">AtualizarUsuarioDTO</span>):
    <span class="pl-s">"""</span>
<span class="pl-s">    Atualiza dados de um usuário.</span>
<span class="pl-s">    """</span>
    <span class="pl-k">try</span>:
        <span class="pl-s1">dados</span> <span class="pl-c1">=</span> <span class="pl-s1">usuario_dto</span>.<span class="pl-c1">to_dict</span>()

        <span class="pl-c"># Atualizar no banco de dados</span>
        <span class="pl-c"># usuario_service.atualizar(id, dados)</span>

        <span class="pl-k">return</span> {<span class="pl-s">"mensagem"</span>: <span class="pl-s">"Usuário atualizado com sucesso"</span>}

    <span class="pl-k">except</span> <span class="pl-v">Exception</span> <span class="pl-k">as</span> <span class="pl-s1">e</span>:
        <span class="pl-k">raise</span> <span class="pl-en">HTTPException</span>(<span class="pl-s1">status_code</span><span class="pl-c1">=</span><span class="pl-c1">400</span>, <span class="pl-s1">detail</span><span class="pl-c1">=</span><span class="pl-en">str</span>(<span class="pl-s1">e</span>))</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="from fastapi import APIRouter, HTTPException
from dtos import CriarUsuarioDTO, AtualizarUsuarioDTO
from pydantic import ValidationError

router = APIRouter()

@router.post(&quot;/usuarios&quot;)
def criar_usuario(usuario_dto: CriarUsuarioDTO):
    &quot;&quot;&quot;
    Cria um novo usuário.

    A validação é automática! Se os dados forem inválidos,
    FastAPI retorna 422 automaticamente.
    &quot;&quot;&quot;
    try:
        # Converter DTO para dict
        dados = usuario_dto.to_dict()

        # Salvar no banco de dados
        # usuario_service.criar(dados)

        return {&quot;mensagem&quot;: &quot;Usuário criado com sucesso&quot;, &quot;dados&quot;: dados}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put(&quot;/usuarios/{id}&quot;)
def atualizar_usuario(id: int, usuario_dto: AtualizarUsuarioDTO):
    &quot;&quot;&quot;
    Atualiza dados de um usuário.
    &quot;&quot;&quot;
    try:
        dados = usuario_dto.to_dict()

        # Atualizar no banco de dados
        # usuario_service.atualizar(id, dados)

        return {&quot;mensagem&quot;: &quot;Usuário atualizado com sucesso&quot;}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Exemplo com Flask:</strong></p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">from</span> <span class="pl-s1">flask</span> <span class="pl-k">import</span> <span class="pl-v">Blueprint</span>, <span class="pl-s1">request</span>, <span class="pl-s1">jsonify</span>
<span class="pl-k">from</span> <span class="pl-s1">dtos</span> <span class="pl-k">import</span> <span class="pl-v">CriarUsuarioDTO</span>
<span class="pl-k">from</span> <span class="pl-s1">pydantic</span> <span class="pl-k">import</span> <span class="pl-v">ValidationError</span>

<span class="pl-s1">usuario_bp</span> <span class="pl-c1">=</span> <span class="pl-en">Blueprint</span>(<span class="pl-s">'usuario'</span>, <span class="pl-s1">__name__</span>)

<span class="pl-en">@<span class="pl-s1">usuario_bp</span>.<span class="pl-c1">route</span>(<span class="pl-s">'/usuarios'</span>, <span class="pl-s1">methods</span><span class="pl-c1">=</span>[<span class="pl-s">'POST'</span>])</span>
<span class="pl-k">def</span> <span class="pl-en">criar_usuario</span>():
    <span class="pl-s">"""</span>
<span class="pl-s">    Cria um novo usuário.</span>
<span class="pl-s">    """</span>
    <span class="pl-k">try</span>:
        <span class="pl-c"># Validar dados com DTO</span>
        <span class="pl-s1">usuario_dto</span> <span class="pl-c1">=</span> <span class="pl-en">CriarUsuarioDTO</span>(<span class="pl-c1">**</span><span class="pl-s1">request</span>.<span class="pl-c1">json</span>)

        <span class="pl-c"># Converter para dict</span>
        <span class="pl-s1">dados</span> <span class="pl-c1">=</span> <span class="pl-s1">usuario_dto</span>.<span class="pl-c1">to_dict</span>()

        <span class="pl-c"># Salvar no banco de dados</span>
        <span class="pl-c"># usuario_service.criar(dados)</span>

        <span class="pl-k">return</span> <span class="pl-en">jsonify</span>({
            <span class="pl-s">"mensagem"</span>: <span class="pl-s">"Usuário criado com sucesso"</span>,
            <span class="pl-s">"dados"</span>: <span class="pl-s1">dados</span>
        }), <span class="pl-c1">201</span>

    <span class="pl-k">except</span> <span class="pl-v">ValidationError</span> <span class="pl-k">as</span> <span class="pl-s1">e</span>:
        <span class="pl-k">return</span> <span class="pl-en">jsonify</span>({<span class="pl-s">"erros"</span>: <span class="pl-s1">e</span>.<span class="pl-c1">errors</span>()}), <span class="pl-c1">422</span>

    <span class="pl-k">except</span> <span class="pl-v">Exception</span> <span class="pl-k">as</span> <span class="pl-s1">e</span>:
        <span class="pl-k">return</span> <span class="pl-en">jsonify</span>({<span class="pl-s">"erro"</span>: <span class="pl-en">str</span>(<span class="pl-s1">e</span>)}), <span class="pl-c1">400</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="from flask import Blueprint, request, jsonify
from dtos import CriarUsuarioDTO
from pydantic import ValidationError

usuario_bp = Blueprint(&#39;usuario&#39;, __name__)

@usuario_bp.route(&#39;/usuarios&#39;, methods=[&#39;POST&#39;])
def criar_usuario():
    &quot;&quot;&quot;
    Cria um novo usuário.
    &quot;&quot;&quot;
    try:
        # Validar dados com DTO
        usuario_dto = CriarUsuarioDTO(**request.json)

        # Converter para dict
        dados = usuario_dto.to_dict()

        # Salvar no banco de dados
        # usuario_service.criar(dados)

        return jsonify({
            &quot;mensagem&quot;: &quot;Usuário criado com sucesso&quot;,
            &quot;dados&quot;: dados
        }), 201

    except ValidationError as e:
        return jsonify({&quot;erros&quot;: e.errors()}), 422

    except Exception as e:
        return jsonify({&quot;erro&quot;: str(e)}), 400" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">📚 Exemplos Práticos</h2><a id="user-content--exemplos-práticos" class="anchor" aria-label="Permalink: 📚 Exemplos Práticos" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#-exemplos-pr%C3%A1ticos"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Exemplo 1: DTO Simples com Validações Básicas</h3><a id="user-content-exemplo-1-dto-simples-com-validações-básicas" class="anchor" aria-label="Permalink: Exemplo 1: DTO Simples com Validações Básicas" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#exemplo-1-dto-simples-com-valida%C3%A7%C3%B5es-b%C3%A1sicas"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">from</span> <span class="pl-s1">pydantic</span> <span class="pl-k">import</span> <span class="pl-v">Field</span>
<span class="pl-k">from</span> .<span class="pl-s1">base_dto</span> <span class="pl-k">import</span> <span class="pl-v">BaseDTO</span>

<span class="pl-k">class</span> <span class="pl-v">ProdutoDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s">"""DTO para cadastro de produto"""</span>

    <span class="pl-s1">nome</span>: <span class="pl-smi">str</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(..., <span class="pl-s1">min_length</span><span class="pl-c1">=</span><span class="pl-c1">3</span>, <span class="pl-s1">max_length</span><span class="pl-c1">=</span><span class="pl-c1">100</span>)
    <span class="pl-s1">preco</span>: <span class="pl-smi">float</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(..., <span class="pl-s1">gt</span><span class="pl-c1">=</span><span class="pl-c1">0</span>)
    <span class="pl-s1">estoque</span>: <span class="pl-smi">int</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(..., <span class="pl-s1">ge</span><span class="pl-c1">=</span><span class="pl-c1">0</span>)
    <span class="pl-s1">ativo</span>: <span class="pl-smi">bool</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(<span class="pl-s1">default</span><span class="pl-c1">=</span><span class="pl-c1">True</span>)</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="from pydantic import Field
from .base_dto import BaseDTO

class ProdutoDTO(BaseDTO):
    &quot;&quot;&quot;DTO para cadastro de produto&quot;&quot;&quot;

    nome: str = Field(..., min_length=3, max_length=100)
    preco: float = Field(..., gt=0)
    estoque: int = Field(..., ge=0)
    ativo: bool = Field(default=True)" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Exemplo 2: DTO com Enum</h3><a id="user-content-exemplo-2-dto-com-enum" class="anchor" aria-label="Permalink: Exemplo 2: DTO com Enum" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#exemplo-2-dto-com-enum"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">from</span> <span class="pl-s1">enum</span> <span class="pl-k">import</span> <span class="pl-v">Enum</span>
<span class="pl-k">from</span> <span class="pl-s1">pydantic</span> <span class="pl-k">import</span> <span class="pl-v">Field</span>, <span class="pl-s1">field_validator</span>
<span class="pl-k">from</span> .<span class="pl-s1">base_dto</span> <span class="pl-k">import</span> <span class="pl-v">BaseDTO</span>
<span class="pl-k">from</span> <span class="pl-s1">util</span>.<span class="pl-s1">validacoes_dto</span> <span class="pl-k">import</span> <span class="pl-s1">validar_enum_valor</span>

<span class="pl-k">class</span> <span class="pl-v">StatusPedido</span>(<span class="pl-s1">str</span>, <span class="pl-v">Enum</span>):
    <span class="pl-c1">PENDENTE</span> <span class="pl-c1">=</span> <span class="pl-s">"PENDENTE"</span>
    <span class="pl-c1">PROCESSANDO</span> <span class="pl-c1">=</span> <span class="pl-s">"PROCESSANDO"</span>
    <span class="pl-c1">ENVIADO</span> <span class="pl-c1">=</span> <span class="pl-s">"ENVIADO"</span>
    <span class="pl-c1">ENTREGUE</span> <span class="pl-c1">=</span> <span class="pl-s">"ENTREGUE"</span>
    <span class="pl-c1">CANCELADO</span> <span class="pl-c1">=</span> <span class="pl-s">"CANCELADO"</span>

<span class="pl-k">class</span> <span class="pl-v">PedidoDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s">"""DTO para pedido"""</span>

    <span class="pl-s1">cliente_id</span>: <span class="pl-smi">int</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(..., <span class="pl-s1">gt</span><span class="pl-c1">=</span><span class="pl-c1">0</span>)
    <span class="pl-s1">status</span>: <span class="pl-smi">StatusPedido</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(<span class="pl-s1">default</span><span class="pl-c1">=</span><span class="pl-v">StatusPedido</span>.<span class="pl-c1">PENDENTE</span>)
    <span class="pl-s1">observacoes</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>] <span class="pl-c1">=</span> <span class="pl-en">Field</span>(<span class="pl-c1">None</span>, <span class="pl-s1">max_length</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)

    <span class="pl-en">@<span class="pl-en">field_validator</span>(<span class="pl-s">'status'</span>)</span>
    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">validar_status</span>(<span class="pl-s1">cls</span>, <span class="pl-s1">v</span>):
        <span class="pl-s1">validador</span> <span class="pl-c1">=</span> <span class="pl-s1">cls</span>.<span class="pl-c1">validar_campo_wrapper</span>(
            <span class="pl-k">lambda</span> <span class="pl-s1">valor</span>, <span class="pl-s1">campo</span>: <span class="pl-en">validar_enum_valor</span>(<span class="pl-s1">valor</span>, <span class="pl-v">StatusPedido</span>, <span class="pl-s1">campo</span>),
            <span class="pl-s">"Status"</span>
        )
        <span class="pl-k">return</span> <span class="pl-en">validador</span>(<span class="pl-s1">v</span>)</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="from enum import Enum
from pydantic import Field, field_validator
from .base_dto import BaseDTO
from util.validacoes_dto import validar_enum_valor

class StatusPedido(str, Enum):
    PENDENTE = &quot;PENDENTE&quot;
    PROCESSANDO = &quot;PROCESSANDO&quot;
    ENVIADO = &quot;ENVIADO&quot;
    ENTREGUE = &quot;ENTREGUE&quot;
    CANCELADO = &quot;CANCELADO&quot;

class PedidoDTO(BaseDTO):
    &quot;&quot;&quot;DTO para pedido&quot;&quot;&quot;

    cliente_id: int = Field(..., gt=0)
    status: StatusPedido = Field(default=StatusPedido.PENDENTE)
    observacoes: Optional[str] = Field(None, max_length=500)

    @field_validator(&#39;status&#39;)
    @classmethod
    def validar_status(cls, v):
        validador = cls.validar_campo_wrapper(
            lambda valor, campo: validar_enum_valor(valor, StatusPedido, campo),
            &quot;Status&quot;
        )
        return validador(v)" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Exemplo 3: DTO com Validação Customizada</h3><a id="user-content-exemplo-3-dto-com-validação-customizada" class="anchor" aria-label="Permalink: Exemplo 3: DTO com Validação Customizada" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#exemplo-3-dto-com-valida%C3%A7%C3%A3o-customizada"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">from</span> <span class="pl-s1">pydantic</span> <span class="pl-k">import</span> <span class="pl-v">Field</span>, <span class="pl-s1">field_validator</span>, <span class="pl-v">ValidationInfo</span>
<span class="pl-k">from</span> .<span class="pl-s1">base_dto</span> <span class="pl-k">import</span> <span class="pl-v">BaseDTO</span>

<span class="pl-k">class</span> <span class="pl-v">AlterarSenhaDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s">"""DTO para alteração de senha"""</span>

    <span class="pl-s1">senha_atual</span>: <span class="pl-smi">str</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(..., <span class="pl-s1">min_length</span><span class="pl-c1">=</span><span class="pl-c1">1</span>)
    <span class="pl-s1">nova_senha</span>: <span class="pl-smi">str</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(..., <span class="pl-s1">min_length</span><span class="pl-c1">=</span><span class="pl-c1">8</span>)
    <span class="pl-s1">confirmar_senha</span>: <span class="pl-smi">str</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(..., <span class="pl-s1">min_length</span><span class="pl-c1">=</span><span class="pl-c1">8</span>)

    <span class="pl-en">@<span class="pl-en">field_validator</span>(<span class="pl-s">'nova_senha'</span>)</span>
    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">validar_nova_senha</span>(<span class="pl-s1">cls</span>, <span class="pl-s1">v</span>: <span class="pl-smi">str</span>, <span class="pl-s1">info</span>: <span class="pl-smi">ValidationInfo</span>) <span class="pl-c1">-&gt;</span> <span class="pl-smi">str</span>:
        <span class="pl-c"># Validar que nova senha é diferente da atual</span>
        <span class="pl-k">if</span> <span class="pl-s">'senha_atual'</span> <span class="pl-c1">in</span> <span class="pl-s1">info</span>.<span class="pl-c1">data</span> <span class="pl-c1">and</span> <span class="pl-s1">v</span> <span class="pl-c1">==</span> <span class="pl-s1">info</span>.<span class="pl-c1">data</span>[<span class="pl-s">'senha_atual'</span>]:
            <span class="pl-k">raise</span> <span class="pl-en">ValueError</span>(<span class="pl-s">'Nova senha deve ser diferente da atual'</span>)

        <span class="pl-c"># Validar força da senha</span>
        <span class="pl-k">if</span> <span class="pl-c1">not</span> <span class="pl-en">any</span>(<span class="pl-s1">c</span>.<span class="pl-c1">isupper</span>() <span class="pl-k">for</span> <span class="pl-s1">c</span> <span class="pl-c1">in</span> <span class="pl-s1">v</span>):
            <span class="pl-k">raise</span> <span class="pl-en">ValueError</span>(<span class="pl-s">'Senha deve conter pelo menos uma letra maiúscula'</span>)

        <span class="pl-k">if</span> <span class="pl-c1">not</span> <span class="pl-en">any</span>(<span class="pl-s1">c</span>.<span class="pl-c1">isdigit</span>() <span class="pl-k">for</span> <span class="pl-s1">c</span> <span class="pl-c1">in</span> <span class="pl-s1">v</span>):
            <span class="pl-k">raise</span> <span class="pl-en">ValueError</span>(<span class="pl-s">'Senha deve conter pelo menos um número'</span>)

        <span class="pl-k">return</span> <span class="pl-s1">v</span>

    <span class="pl-en">@<span class="pl-en">field_validator</span>(<span class="pl-s">'confirmar_senha'</span>)</span>
    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">senhas_devem_coincidir</span>(<span class="pl-s1">cls</span>, <span class="pl-s1">v</span>: <span class="pl-smi">str</span>, <span class="pl-s1">info</span>: <span class="pl-smi">ValidationInfo</span>) <span class="pl-c1">-&gt;</span> <span class="pl-smi">str</span>:
        <span class="pl-k">if</span> <span class="pl-s">'nova_senha'</span> <span class="pl-c1">in</span> <span class="pl-s1">info</span>.<span class="pl-c1">data</span> <span class="pl-c1">and</span> <span class="pl-s1">v</span> <span class="pl-c1">!=</span> <span class="pl-s1">info</span>.<span class="pl-c1">data</span>[<span class="pl-s">'nova_senha'</span>]:
            <span class="pl-k">raise</span> <span class="pl-en">ValueError</span>(<span class="pl-s">'Senhas não coincidem'</span>)
        <span class="pl-k">return</span> <span class="pl-s1">v</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="from pydantic import Field, field_validator, ValidationInfo
from .base_dto import BaseDTO

class AlterarSenhaDTO(BaseDTO):
    &quot;&quot;&quot;DTO para alteração de senha&quot;&quot;&quot;

    senha_atual: str = Field(..., min_length=1)
    nova_senha: str = Field(..., min_length=8)
    confirmar_senha: str = Field(..., min_length=8)

    @field_validator(&#39;nova_senha&#39;)
    @classmethod
    def validar_nova_senha(cls, v: str, info: ValidationInfo) -&gt; str:
        # Validar que nova senha é diferente da atual
        if &#39;senha_atual&#39; in info.data and v == info.data[&#39;senha_atual&#39;]:
            raise ValueError(&#39;Nova senha deve ser diferente da atual&#39;)

        # Validar força da senha
        if not any(c.isupper() for c in v):
            raise ValueError(&#39;Senha deve conter pelo menos uma letra maiúscula&#39;)

        if not any(c.isdigit() for c in v):
            raise ValueError(&#39;Senha deve conter pelo menos um número&#39;)

        return v

    @field_validator(&#39;confirmar_senha&#39;)
    @classmethod
    def senhas_devem_coincidir(cls, v: str, info: ValidationInfo) -&gt; str:
        if &#39;nova_senha&#39; in info.data and v != info.data[&#39;nova_senha&#39;]:
            raise ValueError(&#39;Senhas não coincidem&#39;)
        return v" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Exemplo 4: DTO para Filtros de Listagem</h3><a id="user-content-exemplo-4-dto-para-filtros-de-listagem" class="anchor" aria-label="Permalink: Exemplo 4: DTO para Filtros de Listagem" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#exemplo-4-dto-para-filtros-de-listagem"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">from</span> <span class="pl-s1">typing</span> <span class="pl-k">import</span> <span class="pl-v">Optional</span>
<span class="pl-k">from</span> <span class="pl-s1">pydantic</span> <span class="pl-k">import</span> <span class="pl-v">Field</span>
<span class="pl-k">from</span> .<span class="pl-s1">base_dto</span> <span class="pl-k">import</span> <span class="pl-v">BaseDTO</span>

<span class="pl-k">class</span> <span class="pl-v">ProdutoFiltroDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s">"""DTO para filtros de listagem de produtos"""</span>

    <span class="pl-s1">nome_busca</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>] <span class="pl-c1">=</span> <span class="pl-en">Field</span>(<span class="pl-c1">None</span>, <span class="pl-s1">max_length</span><span class="pl-c1">=</span><span class="pl-c1">100</span>)
    <span class="pl-s1">preco_min</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">float</span>] <span class="pl-c1">=</span> <span class="pl-en">Field</span>(<span class="pl-c1">None</span>, <span class="pl-s1">ge</span><span class="pl-c1">=</span><span class="pl-c1">0</span>)
    <span class="pl-s1">preco_max</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">float</span>] <span class="pl-c1">=</span> <span class="pl-en">Field</span>(<span class="pl-c1">None</span>, <span class="pl-s1">ge</span><span class="pl-c1">=</span><span class="pl-c1">0</span>)
    <span class="pl-s1">ativo</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">bool</span>] <span class="pl-c1">=</span> <span class="pl-c1">None</span>
    <span class="pl-s1">categoria_id</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">int</span>] <span class="pl-c1">=</span> <span class="pl-en">Field</span>(<span class="pl-c1">None</span>, <span class="pl-s1">gt</span><span class="pl-c1">=</span><span class="pl-c1">0</span>)

    <span class="pl-c"># Paginação</span>
    <span class="pl-s1">pagina</span>: <span class="pl-smi">int</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(<span class="pl-s1">default</span><span class="pl-c1">=</span><span class="pl-c1">1</span>, <span class="pl-s1">ge</span><span class="pl-c1">=</span><span class="pl-c1">1</span>)
    <span class="pl-s1">tamanho_pagina</span>: <span class="pl-smi">int</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(<span class="pl-s1">default</span><span class="pl-c1">=</span><span class="pl-c1">20</span>, <span class="pl-s1">ge</span><span class="pl-c1">=</span><span class="pl-c1">1</span>, <span class="pl-s1">le</span><span class="pl-c1">=</span><span class="pl-c1">100</span>)</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="from typing import Optional
from pydantic import Field
from .base_dto import BaseDTO

class ProdutoFiltroDTO(BaseDTO):
    &quot;&quot;&quot;DTO para filtros de listagem de produtos&quot;&quot;&quot;

    nome_busca: Optional[str] = Field(None, max_length=100)
    preco_min: Optional[float] = Field(None, ge=0)
    preco_max: Optional[float] = Field(None, ge=0)
    ativo: Optional[bool] = None
    categoria_id: Optional[int] = Field(None, gt=0)

    # Paginação
    pagina: int = Field(default=1, ge=1)
    tamanho_pagina: int = Field(default=20, ge=1, le=100)" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Exemplo 5: DTO com Relacionamentos</h3><a id="user-content-exemplo-5-dto-com-relacionamentos" class="anchor" aria-label="Permalink: Exemplo 5: DTO com Relacionamentos" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#exemplo-5-dto-com-relacionamentos"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">from</span> <span class="pl-s1">typing</span> <span class="pl-k">import</span> <span class="pl-v">List</span>, <span class="pl-v">Optional</span>
<span class="pl-k">from</span> <span class="pl-s1">pydantic</span> <span class="pl-k">import</span> <span class="pl-v">Field</span>
<span class="pl-k">from</span> .<span class="pl-s1">base_dto</span> <span class="pl-k">import</span> <span class="pl-v">BaseDTO</span>

<span class="pl-k">class</span> <span class="pl-v">ItemPedidoDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s">"""DTO para item do pedido"""</span>

    <span class="pl-s1">produto_id</span>: <span class="pl-smi">int</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(..., <span class="pl-s1">gt</span><span class="pl-c1">=</span><span class="pl-c1">0</span>)
    <span class="pl-s1">quantidade</span>: <span class="pl-smi">int</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(..., <span class="pl-s1">gt</span><span class="pl-c1">=</span><span class="pl-c1">0</span>)
    <span class="pl-s1">preco_unitario</span>: <span class="pl-smi">float</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(..., <span class="pl-s1">gt</span><span class="pl-c1">=</span><span class="pl-c1">0</span>)

<span class="pl-k">class</span> <span class="pl-v">CriarPedidoDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s">"""DTO para criação de pedido com itens"""</span>

    <span class="pl-s1">cliente_id</span>: <span class="pl-smi">int</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(..., <span class="pl-s1">gt</span><span class="pl-c1">=</span><span class="pl-c1">0</span>)
    <span class="pl-s1">itens</span>: <span class="pl-v">List</span>[<span class="pl-smi">ItemPedidoDTO</span>] <span class="pl-c1">=</span> <span class="pl-en">Field</span>(..., <span class="pl-s1">min_length</span><span class="pl-c1">=</span><span class="pl-c1">1</span>)
    <span class="pl-s1">observacoes</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>] <span class="pl-c1">=</span> <span class="pl-en">Field</span>(<span class="pl-c1">None</span>, <span class="pl-s1">max_length</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)

    <span class="pl-en">@<span class="pl-en">field_validator</span>(<span class="pl-s">'itens'</span>)</span>
    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">validar_itens</span>(<span class="pl-s1">cls</span>, <span class="pl-s1">v</span>: <span class="pl-v">List</span>[<span class="pl-smi">ItemPedidoDTO</span>]) <span class="pl-c1">-&gt;</span> <span class="pl-v">List</span>[<span class="pl-smi">ItemPedidoDTO</span>]:
        <span class="pl-k">if</span> <span class="pl-c1">not</span> <span class="pl-s1">v</span>:
            <span class="pl-k">raise</span> <span class="pl-en">ValueError</span>(<span class="pl-s">'Pedido deve ter pelo menos um item'</span>)
        <span class="pl-k">return</span> <span class="pl-s1">v</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="from typing import List, Optional
from pydantic import Field
from .base_dto import BaseDTO

class ItemPedidoDTO(BaseDTO):
    &quot;&quot;&quot;DTO para item do pedido&quot;&quot;&quot;

    produto_id: int = Field(..., gt=0)
    quantidade: int = Field(..., gt=0)
    preco_unitario: float = Field(..., gt=0)

class CriarPedidoDTO(BaseDTO):
    &quot;&quot;&quot;DTO para criação de pedido com itens&quot;&quot;&quot;

    cliente_id: int = Field(..., gt=0)
    itens: List[ItemPedidoDTO] = Field(..., min_length=1)
    observacoes: Optional[str] = Field(None, max_length=500)

    @field_validator(&#39;itens&#39;)
    @classmethod
    def validar_itens(cls, v: List[ItemPedidoDTO]) -&gt; List[ItemPedidoDTO]:
        if not v:
            raise ValueError(&#39;Pedido deve ter pelo menos um item&#39;)
        return v" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">🎯 Boas Práticas</h2><a id="user-content--boas-práticas" class="anchor" aria-label="Permalink: 🎯 Boas Práticas" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#-boas-pr%C3%A1ticas"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">1. <strong>Organize DTOs por Domínio</strong></h3><a id="user-content-1-organize-dtos-por-domínio" class="anchor" aria-label="Permalink: 1. Organize DTOs por Domínio" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#1-organize-dtos-por-dom%C3%ADnio"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-c"># ❌ ERRADO - Um arquivo por DTO</span>
<span class="pl-s1">dtos</span><span class="pl-c1">/</span>
├── <span class="pl-s1">criar_usuario_dto</span>.<span class="pl-c1">py</span>
├── <span class="pl-s1">atualizar_usuario_dto</span>.<span class="pl-c1">py</span>
├── <span class="pl-s1">criar_produto_dto</span>.<span class="pl-c1">py</span>
└── <span class="pl-s1">atualizar_produto_dto</span>.<span class="pl-c1">py</span>

<span class="pl-c"># ✅ CORRETO - Agrupe por domínio</span>
<span class="pl-s1">dtos</span><span class="pl-c1">/</span>
├── <span class="pl-s1">usuario_dtos</span>.<span class="pl-c1">py</span>      <span class="pl-c"># Todos os DTOs de usuário</span>
├── <span class="pl-s1">produto_dtos</span>.<span class="pl-c1">py</span>      <span class="pl-c"># Todos os DTOs de produto</span>
└── <span class="pl-s1">pedido_dtos</span>.<span class="pl-c1">py</span>       <span class="pl-c"># Todos os DTOs de pedido</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="# ❌ ERRADO - Um arquivo por DTO
dtos/
├── criar_usuario_dto.py
├── atualizar_usuario_dto.py
├── criar_produto_dto.py
└── atualizar_produto_dto.py

# ✅ CORRETO - Agrupe por domínio
dtos/
├── usuario_dtos.py      # Todos os DTOs de usuário
├── produto_dtos.py      # Todos os DTOs de produto
└── pedido_dtos.py       # Todos os DTOs de pedido" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">2. <strong>Use Nomes Descritivos</strong></h3><a id="user-content-2-use-nomes-descritivos" class="anchor" aria-label="Permalink: 2. Use Nomes Descritivos" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#2-use-nomes-descritivos"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-c"># ❌ ERRADO</span>
<span class="pl-k">class</span> <span class="pl-v">UsuarioDTO</span>(<span class="pl-v">BaseDTO</span>):  <span class="pl-c"># Muito genérico</span>
    <span class="pl-k">pass</span>

<span class="pl-c"># ✅ CORRETO</span>
<span class="pl-k">class</span> <span class="pl-v">CriarUsuarioDTO</span>(<span class="pl-v">BaseDTO</span>):      <span class="pl-c"># Indica ação e contexto</span>
    <span class="pl-k">pass</span>

<span class="pl-k">class</span> <span class="pl-v">AtualizarUsuarioDTO</span>(<span class="pl-v">BaseDTO</span>):  <span class="pl-c"># Claro e específico</span>
    <span class="pl-k">pass</span>

<span class="pl-k">class</span> <span class="pl-v">UsuarioFiltroDTO</span>(<span class="pl-v">BaseDTO</span>):     <span class="pl-c"># Indica propósito</span>
    <span class="pl-k">pass</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="# ❌ ERRADO
class UsuarioDTO(BaseDTO):  # Muito genérico
    pass

# ✅ CORRETO
class CriarUsuarioDTO(BaseDTO):      # Indica ação e contexto
    pass

class AtualizarUsuarioDTO(BaseDTO):  # Claro e específico
    pass

class UsuarioFiltroDTO(BaseDTO):     # Indica propósito
    pass" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">3. <strong>Documente seus DTOs</strong></h3><a id="user-content-3-documente-seus-dtos" class="anchor" aria-label="Permalink: 3. Documente seus DTOs" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#3-documente-seus-dtos"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">class</span> <span class="pl-v">CriarProdutoDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s">"""</span>
<span class="pl-s">    DTO para criação de novo produto.</span>
<span class="pl-s">    Usado em formulários de cadastro de produtos.</span>
<span class="pl-s"></span>
<span class="pl-s">    Validações:</span>
<span class="pl-s">    - Nome: 3-100 caracteres</span>
<span class="pl-s">    - Preço: Deve ser maior que zero</span>
<span class="pl-s">    - Estoque: Não pode ser negativo</span>
<span class="pl-s">    """</span>

    <span class="pl-s1">nome</span>: <span class="pl-smi">str</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(..., <span class="pl-s1">min_length</span><span class="pl-c1">=</span><span class="pl-c1">3</span>, <span class="pl-s1">max_length</span><span class="pl-c1">=</span><span class="pl-c1">100</span>, <span class="pl-s1">description</span><span class="pl-c1">=</span><span class="pl-s">"Nome do produto"</span>)
    <span class="pl-s1">preco</span>: <span class="pl-smi">float</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(..., <span class="pl-s1">gt</span><span class="pl-c1">=</span><span class="pl-c1">0</span>, <span class="pl-s1">description</span><span class="pl-c1">=</span><span class="pl-s">"Preço unitário (deve ser &gt; 0)"</span>)
    <span class="pl-s1">estoque</span>: <span class="pl-smi">int</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(..., <span class="pl-s1">ge</span><span class="pl-c1">=</span><span class="pl-c1">0</span>, <span class="pl-s1">description</span><span class="pl-c1">=</span><span class="pl-s">"Quantidade em estoque"</span>)</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="class CriarProdutoDTO(BaseDTO):
    &quot;&quot;&quot;
    DTO para criação de novo produto.
    Usado em formulários de cadastro de produtos.

    Validações:
    - Nome: 3-100 caracteres
    - Preço: Deve ser maior que zero
    - Estoque: Não pode ser negativo
    &quot;&quot;&quot;

    nome: str = Field(..., min_length=3, max_length=100, description=&quot;Nome do produto&quot;)
    preco: float = Field(..., gt=0, description=&quot;Preço unitário (deve ser &gt; 0)&quot;)
    estoque: int = Field(..., ge=0, description=&quot;Quantidade em estoque&quot;)" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">4. <strong>Crie Exemplos JSON</strong></h3><a id="user-content-4-crie-exemplos-json" class="anchor" aria-label="Permalink: 4. Crie Exemplos JSON" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#4-crie-exemplos-json"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">class</span> <span class="pl-v">ProdutoDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s1">nome</span>: <span class="pl-smi">str</span>
    <span class="pl-s1">preco</span>: <span class="pl-smi">float</span>

    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">criar_exemplo_json</span>(<span class="pl-s1">cls</span>, <span class="pl-c1">**</span><span class="pl-s1">overrides</span>) <span class="pl-c1">-&gt;</span> <span class="pl-smi">dict</span>:
        <span class="pl-s1">exemplo</span> <span class="pl-c1">=</span> {
            <span class="pl-s">"nome"</span>: <span class="pl-s">"Notebook Dell"</span>,
            <span class="pl-s">"preco"</span>: <span class="pl-c1">3500.00</span>
        }
        <span class="pl-s1">exemplo</span>.<span class="pl-c1">update</span>(<span class="pl-s1">overrides</span>)
        <span class="pl-k">return</span> <span class="pl-s1">exemplo</span>

<span class="pl-c"># Configurar no model_config</span>
<span class="pl-v">ProdutoDTO</span>.<span class="pl-c1">model_config</span>.<span class="pl-c1">update</span>({
    <span class="pl-s">"json_schema_extra"</span>: {
        <span class="pl-s">"example"</span>: <span class="pl-v">ProdutoDTO</span>.<span class="pl-c1">criar_exemplo_json</span>()
    }
})</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="class ProdutoDTO(BaseDTO):
    nome: str
    preco: float

    @classmethod
    def criar_exemplo_json(cls, **overrides) -&gt; dict:
        exemplo = {
            &quot;nome&quot;: &quot;Notebook Dell&quot;,
            &quot;preco&quot;: 3500.00
        }
        exemplo.update(overrides)
        return exemplo

# Configurar no model_config
ProdutoDTO.model_config.update({
    &quot;json_schema_extra&quot;: {
        &quot;example&quot;: ProdutoDTO.criar_exemplo_json()
    }
})" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">5. <strong>Reutilize Validações</strong></h3><a id="user-content-5-reutilize-validações" class="anchor" aria-label="Permalink: 5. Reutilize Validações" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#5-reutilize-valida%C3%A7%C3%B5es"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-c"># ❌ ERRADO - Repetir validação em cada DTO</span>
<span class="pl-k">class</span> <span class="pl-v">UsuarioDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s1">cpf</span>: <span class="pl-smi">str</span>

    <span class="pl-en">@<span class="pl-en">field_validator</span>(<span class="pl-s">'cpf'</span>)</span>
    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">validar_cpf</span>(<span class="pl-s1">cls</span>, <span class="pl-s1">v</span>):
        <span class="pl-c"># ... código de validação repetido ...</span>
        <span class="pl-k">pass</span>

<span class="pl-c"># ✅ CORRETO - Usar função centralizada</span>
<span class="pl-k">from</span> <span class="pl-s1">util</span>.<span class="pl-s1">validacoes_dto</span> <span class="pl-k">import</span> <span class="pl-s1">validar_cpf</span>

<span class="pl-k">class</span> <span class="pl-v">UsuarioDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s1">cpf</span>: <span class="pl-smi">str</span>

    <span class="pl-en">@<span class="pl-en">field_validator</span>(<span class="pl-s">'cpf'</span>)</span>
    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">validar_cpf_campo</span>(<span class="pl-s1">cls</span>, <span class="pl-s1">v</span>):
        <span class="pl-s1">validador</span> <span class="pl-c1">=</span> <span class="pl-s1">cls</span>.<span class="pl-c1">validar_campo_wrapper</span>(
            <span class="pl-k">lambda</span> <span class="pl-s1">valor</span>, <span class="pl-s1">campo</span>: <span class="pl-en">validar_cpf</span>(<span class="pl-s1">valor</span>),
            <span class="pl-s">"CPF"</span>
        )
        <span class="pl-k">return</span> <span class="pl-en">validador</span>(<span class="pl-s1">v</span>)</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="# ❌ ERRADO - Repetir validação em cada DTO
class UsuarioDTO(BaseDTO):
    cpf: str

    @field_validator(&#39;cpf&#39;)
    @classmethod
    def validar_cpf(cls, v):
        # ... código de validação repetido ...
        pass

# ✅ CORRETO - Usar função centralizada
from util.validacoes_dto import validar_cpf

class UsuarioDTO(BaseDTO):
    cpf: str

    @field_validator(&#39;cpf&#39;)
    @classmethod
    def validar_cpf_campo(cls, v):
        validador = cls.validar_campo_wrapper(
            lambda valor, campo: validar_cpf(valor),
            &quot;CPF&quot;
        )
        return validador(v)" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">6. <strong>Separe DTOs de Models</strong></h3><a id="user-content-6-separe-dtos-de-models" class="anchor" aria-label="Permalink: 6. Separe DTOs de Models" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#6-separe-dtos-de-models"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-c"># Model (banco de dados)</span>
<span class="pl-k">class</span> <span class="pl-v">Usuario</span>:
    <span class="pl-s1">id</span>: <span class="pl-smi">int</span>
    <span class="pl-s1">nome</span>: <span class="pl-smi">str</span>
    <span class="pl-s1">email</span>: <span class="pl-smi">str</span>
    <span class="pl-s1">senha_hash</span>: <span class="pl-smi">str</span>  <span class="pl-c"># Senha criptografada</span>
    <span class="pl-s1">criado_em</span>: <span class="pl-smi">datetime</span>
    <span class="pl-s1">atualizado_em</span>: <span class="pl-smi">datetime</span>

<span class="pl-c"># DTO (API/Formulário)</span>
<span class="pl-k">class</span> <span class="pl-v">CriarUsuarioDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s1">nome</span>: <span class="pl-smi">str</span>
    <span class="pl-s1">email</span>: <span class="pl-smi">EmailStr</span>
    <span class="pl-s1">senha</span>: <span class="pl-smi">str</span>  <span class="pl-c"># Senha em texto plano (será criptografada)</span>
    <span class="pl-c"># Não expõe dados internos como senha_hash ou timestamps</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="# Model (banco de dados)
class Usuario:
    id: int
    nome: str
    email: str
    senha_hash: str  # Senha criptografada
    criado_em: datetime
    atualizado_em: datetime

# DTO (API/Formulário)
class CriarUsuarioDTO(BaseDTO):
    nome: str
    email: EmailStr
    senha: str  # Senha em texto plano (será criptografada)
    # Não expõe dados internos como senha_hash ou timestamps" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">7. <strong>Use Tipos Adequados</strong></h3><a id="user-content-7-use-tipos-adequados" class="anchor" aria-label="Permalink: 7. Use Tipos Adequados" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#7-use-tipos-adequados"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">from</span> <span class="pl-s1">pydantic</span> <span class="pl-k">import</span> <span class="pl-v">EmailStr</span>, <span class="pl-v">HttpUrl</span>, <span class="pl-s1">conint</span>, <span class="pl-s1">condecimal</span>
<span class="pl-k">from</span> <span class="pl-s1">datetime</span> <span class="pl-k">import</span> <span class="pl-s1">date</span>, <span class="pl-s1">datetime</span>
<span class="pl-k">from</span> <span class="pl-s1">decimal</span> <span class="pl-k">import</span> <span class="pl-v">Decimal</span>

<span class="pl-k">class</span> <span class="pl-v">ExemploDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-c"># ✅ Use EmailStr para emails</span>
    <span class="pl-s1">email</span>: <span class="pl-smi">EmailStr</span>

    <span class="pl-c"># ✅ Use HttpUrl para URLs</span>
    <span class="pl-s1">website</span>: <span class="pl-smi">HttpUrl</span>

    <span class="pl-c"># ✅ Use Decimal para valores monetários</span>
    <span class="pl-s1">preco</span>: <span class="pl-smi">Decimal</span>

    <span class="pl-c"># ✅ Use date/datetime para datas</span>
    <span class="pl-s1">data_nascimento</span>: <span class="pl-smi">date</span>
    <span class="pl-s1">data_cadastro</span>: <span class="pl-smi">datetime</span>

    <span class="pl-c"># ✅ Use constrained types para validações específicas</span>
    <span class="pl-s1">idade</span>: <span class="pl-en">conint</span>(<span class="pl-s1">ge</span><span class="pl-c1">=</span><span class="pl-c1">18</span>, <span class="pl-s1">le</span><span class="pl-c1">=</span><span class="pl-c1">120</span>)  <span class="pl-c"># Entre 18 e 120</span>
    <span class="pl-s1">desconto</span>: <span class="pl-en">condecimal</span>(<span class="pl-s1">ge</span><span class="pl-c1">=</span><span class="pl-c1">0</span>, <span class="pl-s1">le</span><span class="pl-c1">=</span><span class="pl-c1">100</span>)  <span class="pl-c"># Entre 0 e 100</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="from pydantic import EmailStr, HttpUrl, conint, condecimal
from datetime import date, datetime
from decimal import Decimal

class ExemploDTO(BaseDTO):
    # ✅ Use EmailStr para emails
    email: EmailStr

    # ✅ Use HttpUrl para URLs
    website: HttpUrl

    # ✅ Use Decimal para valores monetários
    preco: Decimal

    # ✅ Use date/datetime para datas
    data_nascimento: date
    data_cadastro: datetime

    # ✅ Use constrained types para validações específicas
    idade: conint(ge=18, le=120)  # Entre 18 e 120
    desconto: condecimal(ge=0, le=100)  # Entre 0 e 100" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">8. <strong>Trate Campos Opcionais Corretamente</strong></h3><a id="user-content-8-trate-campos-opcionais-corretamente" class="anchor" aria-label="Permalink: 8. Trate Campos Opcionais Corretamente" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#8-trate-campos-opcionais-corretamente"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">from</span> <span class="pl-s1">typing</span> <span class="pl-k">import</span> <span class="pl-v">Optional</span>

<span class="pl-k">class</span> <span class="pl-v">ProdutoDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-c"># Campo obrigatório</span>
    <span class="pl-s1">nome</span>: <span class="pl-smi">str</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(...)

    <span class="pl-c"># Campo opcional com valor padrão</span>
    <span class="pl-s1">ativo</span>: <span class="pl-smi">bool</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(<span class="pl-s1">default</span><span class="pl-c1">=</span><span class="pl-c1">True</span>)

    <span class="pl-c"># Campo opcional sem valor padrão</span>
    <span class="pl-s1">descricao</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>] <span class="pl-c1">=</span> <span class="pl-en">Field</span>(<span class="pl-c1">None</span>)

    <span class="pl-c"># Validar apenas se campo foi fornecido</span>
    <span class="pl-en">@<span class="pl-en">field_validator</span>(<span class="pl-s">'descricao'</span>)</span>
    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">validar_descricao</span>(<span class="pl-s1">cls</span>, <span class="pl-s1">v</span>: <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>]) <span class="pl-c1">-&gt;</span> <span class="pl-v">Optional</span>[<span class="pl-smi">str</span>]:
        <span class="pl-k">if</span> <span class="pl-s1">v</span> <span class="pl-c1">is</span> <span class="pl-c1">None</span>:
            <span class="pl-k">return</span> <span class="pl-s1">v</span>
        <span class="pl-c"># Validar apenas se não for None</span>
        <span class="pl-k">if</span> <span class="pl-en">len</span>(<span class="pl-s1">v</span>) <span class="pl-c1">&lt;</span> <span class="pl-c1">10</span>:
            <span class="pl-k">raise</span> <span class="pl-en">ValueError</span>(<span class="pl-s">'Descrição muito curta'</span>)
        <span class="pl-k">return</span> <span class="pl-s1">v</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="from typing import Optional

class ProdutoDTO(BaseDTO):
    # Campo obrigatório
    nome: str = Field(...)

    # Campo opcional com valor padrão
    ativo: bool = Field(default=True)

    # Campo opcional sem valor padrão
    descricao: Optional[str] = Field(None)

    # Validar apenas se campo foi fornecido
    @field_validator(&#39;descricao&#39;)
    @classmethod
    def validar_descricao(cls, v: Optional[str]) -&gt; Optional[str]:
        if v is None:
            return v
        # Validar apenas se não for None
        if len(v) &lt; 10:
            raise ValueError(&#39;Descrição muito curta&#39;)
        return v" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">🔧 Troubleshooting</h2><a id="user-content--troubleshooting" class="anchor" aria-label="Permalink: 🔧 Troubleshooting" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#-troubleshooting"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Problema 1: "ValidationError: field required"</h3><a id="user-content-problema-1-validationerror-field-required" class="anchor" aria-label="Permalink: Problema 1: &quot;ValidationError: field required&quot;" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#problema-1-validationerror-field-required"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong>Causa:</strong> Campo obrigatório não foi fornecido</p>
<p dir="auto"><strong>Solução:</strong></p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-c"># Certifique-se de que campos obrigatórios usam ... (Ellipsis)</span>
<span class="pl-k">class</span> <span class="pl-v">UsuarioDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s1">nome</span>: <span class="pl-smi">str</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(...)  <span class="pl-c"># Obrigatório</span>
    <span class="pl-s1">email</span>: <span class="pl-smi">EmailStr</span> <span class="pl-c1">=</span> <span class="pl-en">Field</span>(...)  <span class="pl-c"># Obrigatório</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="# Certifique-se de que campos obrigatórios usam ... (Ellipsis)
class UsuarioDTO(BaseDTO):
    nome: str = Field(...)  # Obrigatório
    email: EmailStr = Field(...)  # Obrigatório" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Problema 2: "ImportError: cannot import name 'ValidacaoError'"</h3><a id="user-content-problema-2-importerror-cannot-import-name-validacaoerror" class="anchor" aria-label="Permalink: Problema 2: &quot;ImportError: cannot import name &#39;ValidacaoError&#39;&quot;" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#problema-2-importerror-cannot-import-name-validacaoerror"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong>Causa:</strong> Módulo de validações não encontrado</p>
<p dir="auto"><strong>Solução:</strong></p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-c"># Verifique o caminho correto para o módulo</span>
<span class="pl-k">from</span> <span class="pl-s1">util</span>.<span class="pl-s1">validacoes_dto</span> <span class="pl-k">import</span> <span class="pl-v">ValidacaoError</span>  <span class="pl-c"># Ajuste o caminho conforme sua estrutura</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="# Verifique o caminho correto para o módulo
from util.validacoes_dto import ValidacaoError  # Ajuste o caminho conforme sua estrutura" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Problema 3: Validação não está sendo executada</h3><a id="user-content-problema-3-validação-não-está-sendo-executada" class="anchor" aria-label="Permalink: Problema 3: Validação não está sendo executada" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#problema-3-valida%C3%A7%C3%A3o-n%C3%A3o-est%C3%A1-sendo-executada"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong>Causa:</strong> Esqueceu de usar @field_validator</p>
<p dir="auto"><strong>Solução:</strong></p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">class</span> <span class="pl-v">UsuarioDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s1">cpf</span>: <span class="pl-smi">str</span>

    <span class="pl-c"># ✅ Adicione o decorator</span>
    <span class="pl-en">@<span class="pl-en">field_validator</span>(<span class="pl-s">'cpf'</span>)</span>
    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">validar_cpf</span>(<span class="pl-s1">cls</span>, <span class="pl-s1">v</span>):
        <span class="pl-c"># ... validação ...</span>
        <span class="pl-k">pass</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="class UsuarioDTO(BaseDTO):
    cpf: str

    # ✅ Adicione o decorator
    @field_validator(&#39;cpf&#39;)
    @classmethod
    def validar_cpf(cls, v):
        # ... validação ...
        pass" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Problema 4: "ValueError: Extra inputs are not permitted"</h3><a id="user-content-problema-4-valueerror-extra-inputs-are-not-permitted" class="anchor" aria-label="Permalink: Problema 4: &quot;ValueError: Extra inputs are not permitted&quot;" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#problema-4-valueerror-extra-inputs-are-not-permitted"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong>Causa:</strong> DTO recebeu campos não declarados</p>
<p dir="auto"><strong>Solução:</strong></p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-c"># Opção 1: Permitir campos extras (não recomendado)</span>
<span class="pl-k">class</span> <span class="pl-v">UsuarioDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s1">model_config</span> <span class="pl-c1">=</span> <span class="pl-en">ConfigDict</span>(<span class="pl-s1">extra</span><span class="pl-c1">=</span><span class="pl-s">'allow'</span>)

<span class="pl-c"># Opção 2: Ignorar campos extras (recomendado)</span>
<span class="pl-k">class</span> <span class="pl-v">UsuarioDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s1">model_config</span> <span class="pl-c1">=</span> <span class="pl-en">ConfigDict</span>(<span class="pl-s1">extra</span><span class="pl-c1">=</span><span class="pl-s">'ignore'</span>)

<span class="pl-c"># Opção 3: Proibir campos extras (padrão, mais seguro)</span>
<span class="pl-k">class</span> <span class="pl-v">UsuarioDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s1">model_config</span> <span class="pl-c1">=</span> <span class="pl-en">ConfigDict</span>(<span class="pl-s1">extra</span><span class="pl-c1">=</span><span class="pl-s">'forbid'</span>)</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="# Opção 1: Permitir campos extras (não recomendado)
class UsuarioDTO(BaseDTO):
    model_config = ConfigDict(extra=&#39;allow&#39;)

# Opção 2: Ignorar campos extras (recomendado)
class UsuarioDTO(BaseDTO):
    model_config = ConfigDict(extra=&#39;ignore&#39;)

# Opção 3: Proibir campos extras (padrão, mais seguro)
class UsuarioDTO(BaseDTO):
    model_config = ConfigDict(extra=&#39;forbid&#39;)" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Problema 5: Enum não aceita valores</h3><a id="user-content-problema-5-enum-não-aceita-valores" class="anchor" aria-label="Permalink: Problema 5: Enum não aceita valores" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#problema-5-enum-n%C3%A3o-aceita-valores"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong>Causa:</strong> Valor enviado não corresponde aos valores do Enum</p>
<p dir="auto"><strong>Solução:</strong></p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">from</span> <span class="pl-s1">enum</span> <span class="pl-k">import</span> <span class="pl-v">Enum</span>

<span class="pl-k">class</span> <span class="pl-v">StatusEnum</span>(<span class="pl-s1">str</span>, <span class="pl-v">Enum</span>):
    <span class="pl-c1">ATIVO</span> <span class="pl-c1">=</span> <span class="pl-s">"ATIVO"</span>
    <span class="pl-c1">INATIVO</span> <span class="pl-c1">=</span> <span class="pl-s">"INATIVO"</span>

<span class="pl-c"># ✅ Configure use_enum_values=True no model_config</span>
<span class="pl-k">class</span> <span class="pl-v">ProdutoDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s1">status</span>: <span class="pl-smi">StatusEnum</span>

    <span class="pl-s1">model_config</span> <span class="pl-c1">=</span> <span class="pl-en">ConfigDict</span>(<span class="pl-s1">use_enum_values</span><span class="pl-c1">=</span><span class="pl-c1">True</span>)</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="from enum import Enum

class StatusEnum(str, Enum):
    ATIVO = &quot;ATIVO&quot;
    INATIVO = &quot;INATIVO&quot;

# ✅ Configure use_enum_values=True no model_config
class ProdutoDTO(BaseDTO):
    status: StatusEnum

    model_config = ConfigDict(use_enum_values=True)" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Problema 6: Validação de senha não compara com outro campo</h3><a id="user-content-problema-6-validação-de-senha-não-compara-com-outro-campo" class="anchor" aria-label="Permalink: Problema 6: Validação de senha não compara com outro campo" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#problema-6-valida%C3%A7%C3%A3o-de-senha-n%C3%A3o-compara-com-outro-campo"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong>Causa:</strong> Não está usando ValidationInfo</p>
<p dir="auto"><strong>Solução:</strong></p>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">from</span> <span class="pl-s1">pydantic</span> <span class="pl-k">import</span> <span class="pl-s1">field_validator</span>, <span class="pl-v">ValidationInfo</span>

<span class="pl-k">class</span> <span class="pl-v">AlterarSenhaDTO</span>(<span class="pl-v">BaseDTO</span>):
    <span class="pl-s1">nova_senha</span>: <span class="pl-smi">str</span>
    <span class="pl-s1">confirmar_senha</span>: <span class="pl-smi">str</span>

    <span class="pl-en">@<span class="pl-en">field_validator</span>(<span class="pl-s">'confirmar_senha'</span>)</span>
    <span class="pl-en">@<span class="pl-s1">classmethod</span></span>
    <span class="pl-k">def</span> <span class="pl-en">senhas_coincidem</span>(<span class="pl-s1">cls</span>, <span class="pl-s1">v</span>: <span class="pl-smi">str</span>, <span class="pl-s1">info</span>: <span class="pl-smi">ValidationInfo</span>) <span class="pl-c1">-&gt;</span> <span class="pl-smi">str</span>:
        <span class="pl-k">if</span> <span class="pl-s">'nova_senha'</span> <span class="pl-c1">in</span> <span class="pl-s1">info</span>.<span class="pl-c1">data</span> <span class="pl-c1">and</span> <span class="pl-s1">v</span> <span class="pl-c1">!=</span> <span class="pl-s1">info</span>.<span class="pl-c1">data</span>[<span class="pl-s">'nova_senha'</span>]:
            <span class="pl-k">raise</span> <span class="pl-en">ValueError</span>(<span class="pl-s">'Senhas não coincidem'</span>)
        <span class="pl-k">return</span> <span class="pl-s1">v</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="from pydantic import field_validator, ValidationInfo

class AlterarSenhaDTO(BaseDTO):
    nova_senha: str
    confirmar_senha: str

    @field_validator(&#39;confirmar_senha&#39;)
    @classmethod
    def senhas_coincidem(cls, v: str, info: ValidationInfo) -&gt; str:
        if &#39;nova_senha&#39; in info.data and v != info.data[&#39;nova_senha&#39;]:
            raise ValueError(&#39;Senhas não coincidem&#39;)
        return v" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">📚 Recursos Adicionais</h2><a id="user-content--recursos-adicionais" class="anchor" aria-label="Permalink: 📚 Recursos Adicionais" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#-recursos-adicionais"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Documentação Oficial:</h3><a id="user-content-documentação-oficial" class="anchor" aria-label="Permalink: Documentação Oficial:" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#documenta%C3%A7%C3%A3o-oficial"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul dir="auto">
<li><strong>Pydantic:</strong> <a href="https://docs.pydantic.dev/" rel="nofollow">https://docs.pydantic.dev/</a></li>
<li><strong>FastAPI:</strong> <a href="https://fastapi.tiangolo.com/" rel="nofollow">https://fastapi.tiangolo.com/</a></li>
<li><strong>Python Type Hints:</strong> <a href="https://docs.python.org/3/library/typing.html" rel="nofollow">https://docs.python.org/3/library/typing.html</a></li>
</ul>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Exemplos de Validações Comuns:</h3><a id="user-content-exemplos-de-validações-comuns" class="anchor" aria-label="Permalink: Exemplos de Validações Comuns:" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#exemplos-de-valida%C3%A7%C3%B5es-comuns"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul dir="auto">
<li>CPF/CNPJ: <a href="https://github.com/brazilians/validators">https://github.com/brazilians/validators</a></li>
<li>CEP: <a href="https://pycep-correios.readthedocs.io/" rel="nofollow">https://pycep-correios.readthedocs.io/</a></li>
<li>Telefone: <a href="https://github.com/daviddrysdale/python-phonenumbers">https://github.com/daviddrysdale/python-phonenumbers</a></li>
</ul>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Padrões de Projeto:</h3><a id="user-content-padrões-de-projeto" class="anchor" aria-label="Permalink: Padrões de Projeto:" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#padr%C3%B5es-de-projeto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul dir="auto">
<li><strong>DTO Pattern:</strong> <a href="https://martinfowler.com/eaaCatalog/dataTransferObject.html" rel="nofollow">https://martinfowler.com/eaaCatalog/dataTransferObject.html</a></li>
<li><strong>Validation Pattern:</strong> <a href="https://refactoring.guru/design-patterns/specification" rel="nofollow">https://refactoring.guru/design-patterns/specification</a></li>
</ul>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">✅ Checklist de Implementação</h2><a id="user-content--checklist-de-implementação" class="anchor" aria-label="Permalink: ✅ Checklist de Implementação" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#-checklist-de-implementa%C3%A7%C3%A3o"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Instalar Pydantic (<code>pip install pydantic[email]</code>)</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Criar estrutura de diretórios (<code>dtos/</code>, <code>util/</code>)</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Implementar <code>ValidacaoError</code> em <code>util/validacoes_dto.py</code></li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Criar funções de validação em <code>util/validacoes_dto.py</code></li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Implementar <code>ValidadorWrapper</code> em <code>util/validacoes_dto.py</code></li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Criar <code>BaseDTO</code> em <code>dtos/base_dto.py</code></li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Criar primeiro DTO por domínio (ex: <code>usuario_dtos.py</code>)</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Configurar <code>dtos/__init__.py</code> com imports facilitados</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Usar DTOs nas rotas/controllers</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Testar validações com dados inválidos</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Documentar DTOs com docstrings</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Criar exemplos JSON para documentação da API</li>
</ul>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">🎓 Conclusão</h2><a id="user-content--conclusão" class="anchor" aria-label="Permalink: 🎓 Conclusão" href="https://github.com/maroquio/LojaVirtual_2025/blob/main/DTO.md#-conclus%C3%A3o"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Este manual fornece tudo que você precisa para implementar DTOs de forma profissional em seu projeto Python. Seguindo este padrão, você terá:</p>
<p dir="auto">✅ <strong>Validação automática</strong> de todos os dados de entrada
✅ <strong>Código organizado</strong> e fácil de manter
✅ <strong>Documentação automática</strong> da API
✅ <strong>Segurança</strong> contra dados inválidos
✅ <strong>Reutilização</strong> de código através de funções centralizadas</p>
<p dir="auto"><strong>Próximos passos sugeridos:</strong></p>
<ol dir="auto">
<li>Implemente a estrutura base (Passos 1-6)</li>
<li>Crie seu primeiro DTO seguindo os exemplos</li>
<li>Teste com dados válidos e inválidos</li>
<li>Expanda gradualmente para outros domínios do sistema</li>
</ol>
<p dir="auto"><strong>Dúvidas?</strong> Consulte os exemplos práticos e o troubleshooting neste manual.</p>
<hr>
<p dir="auto"><strong>Baseado no projeto CaseBem</strong> - Sistema de gerenciamento de casamentos
<strong>Última atualização:</strong> 2025
<strong>Versão:</strong> 1.0</p>
</article></div><button hidden="" data-hotkey="Control+a"></button></section></div></div></div>   </div></div></div></div></div></div></div><div id="find-result-marks-container" class="Box-sc-g0xbh4-0 cCoXib"></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+F6,Control+Shift+F6"></button><button hidden="" data-hotkey="Control+F6,Control+Shift+F6"></button></div> <!-- --> <!-- --> <script type="application/json" id="__PRIMER_DATA_:R0:__">{"resolvedServerColorMode":"day"}</script></div>
</react-app>




  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer pt-8 pb-6 f6 color-fg-muted p-responsive" role="contentinfo" hidden="">
  <h2 class="sr-only">Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="GitHub Homepage" class="footer-octicon mr-2" href="https://github.com/">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12 1C5.923 1 1 5.923 1 12c0 4.867 3.149 8.979 7.521 10.436.55.096.756-.233.756-.522 0-.262-.013-1.128-.013-2.049-2.764.509-3.479-.674-3.699-1.292-.124-.317-.66-1.293-1.127-1.554-.385-.207-.936-.715-.014-.729.866-.014 1.485.797 1.691 1.128.99 1.663 2.571 1.196 3.204.907.096-.715.385-1.196.701-1.471-2.448-.275-5.005-1.224-5.005-5.432 0-1.196.426-2.186 1.128-2.956-.111-.275-.496-1.402.11-2.915 0 0 .921-.288 3.024 1.128a10.193 10.193 0 0 1 2.75-.371c.936 0 1.871.123 2.75.371 2.104-1.43 3.025-1.128 3.025-1.128.605 1.513.221 2.64.111 2.915.701.77 1.127 1.747 1.127 2.956 0 4.222-2.571 5.157-5.019 5.432.399.344.743 1.004.743 2.035 0 1.471-.014 2.654-.014 3.025 0 .289.206.632.756.522C19.851 20.979 23 16.854 23 12c0-6.077-4.922-11-11-11Z"></path>
</svg>
</a>
      <span>
        © 2025 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to community&quot;,&quot;label&quot;:&quot;text:community&quot;}" href="https://github.community/" data-view-component="true" class="Link--secondary Link">Community</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com/?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;cookies&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;cookies_link_subfooter_footer&quot;}">
       Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent text-left" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;dont_share_info&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;dont_share_info_link_subfooter_footer&quot;}">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>



    <ghcc-consent id="ghcc" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-locale="en" data-initial-cookie-consent-allowed="" data-cookie-consent-required="true" data-catalyst=""></ghcc-consent>




  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>


    <style>
      .user-mention[href$="/FernandaBighi"] {
        color: var(--color-user-mention-fg);
        background-color: var(--bgColor-attention-muted, var(--color-attention-subtle));
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
      }
      .user-mention[href$="/FernandaBighi"]:before,
      .user-mention[href$="/FernandaBighi"]:after {
        content: '';
        display: inline-block;
        width: 2px;
      }
    </style>


    </div>
    <div id="js-global-screen-reader-notice" class="sr-only mt-n1" aria-live="polite" aria-atomic="true">LojaVirtual_2025/DTO.md at main · maroquio/LojaVirtual_2025</div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only mt-n1" aria-live="assertive" aria-atomic="true"></div>
  


<div class="sr-only mt-n1" id="screenReaderAnnouncementDiv" role="alert" data-testid="screenReaderAnnouncement" aria-live="assertive"></div></body></html>