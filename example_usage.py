from client import EnterpriseSyntheticPresenterVideoScriptPipelineClient

def main():
    client = EnterpriseSyntheticPresenterVideoScriptPipelineClient()
    res = client.generate_corporate_training_video_suite('Enterprise AI Governance and Compliance Onboarding', 5, ['EN', 'FR', 'ES', 'ZH'])
    print('Video Suite: ' + res['video_suite_id'] + ' | ' + res['course_title'])
    print('Modules: ' + str(res['total_modules_rendered']) + ' rendered in ' + str(res['video_rendering_duration_minutes']) + ' mins across ' + ', '.join(res['localization_languages']))
    print('SCORM Ready: ' + str(res['scorm_lms_compliance_package_ready']) + ' | URL: ' + res['lms_bundle_zip_url'])

if __name__ == '__main__':
    main()
