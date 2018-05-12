/* labels */

$('.status:contains("Risk Approved") span').removeClass('openRisk').addClass('acceptedRisk');
$('.statusR:contains("Risk Approved") span').removeClass('riskStatus').addClass('riskStatus');

$('.typeR:contains("RISK") span').removeClass('riskType').addClass('riskType');
$('.typeR:contains("VULN") span').removeClass('riskType').addClass('vulnType');
$('.typeR:contains("SEC") span').removeClass('riskType').addClass('incidentType');
$('.typeR:contains("BABEL") span').removeClass('riskType').addClass('incidentType');
$('.typeR:contains("GDPR") span').removeClass('riskType').addClass('gdprType');

$('.typeR:contains("Task") span').removeClass('riskType').addClass('taskType');
$('.typeR:contains("Epic") span').removeClass('riskType').addClass('epicType');
$('.typeR:contains("Programme") span').removeClass('riskType').addClass('progType');
$('.typeR:contains("Project") span').removeClass('riskType').addClass('projType');


