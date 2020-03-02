### Datasets References:

## Datasets within the Hackathon Challenge Briefing that were used in the analysis

* Prescription dataset (https://openprescribing.net/api/) - we access the stem type '0411' which corresponds to dementia. The prepared data is in the quantity of medications. We also accessed medication quantity from Obesity (sub category Diabetes can be seen as a risk factor for Dementia), Alcohol Dependence and Nicotine Dependence (These two can be seen as proxy data for smoking and drinking behaviours which are also risk factors for Dementia)

* GP work force data from (https://app.powerbi.com/view?r=eyJrIjoiNmY4NGNiMWQtMGVkZi00MzU2LThiZGMtMTFlZjY2NGE0NTZmIiwidCI6IjUwZjYwNzFmLWJiZmUtNDAxYS04ODAzLTY3Mzc0OGU2MjllMiIsImMiOjh9) - the intention was to find out about GP work force split by ethinicity group at each pratice but this didn't work out. We can split the GP work force on gender though.

* NHS Stop Smoking data is also explored (https://digital.nhs.uk/data-and-information/publications/statistical/statistics-on-nhs-stop-smoking-services-in-england) but these were not used to proximate the smoking behaviour because the number of people are sparse and hard to join past data together (highly manual process). Instad the ONS data is consulted, adult smoking habits (https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/drugusealcoholandsmoking/datasets/adultsmokinghabitsingreatbritain) and (https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/drugusealcoholandsmoking/datasets/adultdrinkinghabits). The general trend is slowly dropping for the population group (65+) we are concerned with so we opted for prescription data as an estimate of the local behaviour in the CCG


## Datasets outside of the Hackathon Challenge Briefing

* Recorded Dementia Diagnoses (https://digital.nhs.uk/data-and-information/publications/statistical/recorded-dementia-diagnoses). Data are manually scraped from this page going back in 3-4 years on Number of Diagnosed patients registered by CCG by ethinicity.

* Prevalence for each practice for Dementia (https://qof.digital.nhs.uk/). Prevalance for all disease codes that are included in the Quality and Outcomes Framework (QOF) which is a voluntary annual reward and incentive programme for all GP surgeries in England, detailing practice achievement results. 

* Population data by CCGs from Office for National Statistics (https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/clinicalcommissioninggroupmidyearpopulationestimates)

* Population estimates from 2016 looking into the future by CCGs from Office for National Statistics (https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/datasets/clinicalcommissioninggroupsinenglandtable3)

* Social Deprivation stats: in the report (https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/733065/Dying_with_dementia_data_analysis_report.pdf) Social deprivation is highlighted as a factor contributing to Dementia death especially for the most deprived, the death rate is twice as high as people who are midly deprived.

* 2011 Census data ethinic group by age (https://www.ons.gov.uk/census/2011census/2011censusdata/2011censusdatacatalogue) - thsi is extracted to analyse if some of the CCGs are underserving some ethinic groups or not recording enough data to know. This can highlight some needs for outreach need within the CCGs.



