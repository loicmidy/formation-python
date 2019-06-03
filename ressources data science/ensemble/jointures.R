sifa<-data.frame(nom_sifa = c('nom_a','nom_b'),prenom_sifa = c('prenom_a','prenom_b'),INE = c('AAAA','BBB'))
mmo<-data.frame(nom_mmo=c('nom_a','nom_c'),prenom_mmo=c('prenom_a','prenom_c'),salaire=c(10,9))

library(tidyverse)


sifa_mmo_inner_join= inner_join(sifa,mmo,by = c("nom_sifa" ="nom_mmo","prenom_sifa" = "prenom_mmo"))
sifa_mmo_left_join= left_join(sifa,mmo,by = c("nom_sifa" ="nom_mmo","prenom_sifa" = "prenom_mmo"))
sifa_mmo_right_join=right_join(sifa,mmo,by = c("nom_sifa" ="nom_mmo","prenom_sifa" = "prenom_mmo"))
sifa_mmo_outer_join=full_join(sifa,mmo,by = c("nom_sifa" ="nom_mmo","prenom_sifa" = "prenom_mmo"))


tips=arrange(tips,sex,desc(total_bill))

tips.sort_values(['sex', 'total_bill'],ascending=[True,False],inplace=True)