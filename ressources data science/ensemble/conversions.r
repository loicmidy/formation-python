library(readr)
notesElevesMatières<-read_delim("C:/Users/loicm/ressources data science/ensemble/eleves.csv",
                                delim="|",
                                col_types=cols(
                                  élève = col_character(),
                                  moyenneMath=col_double(),
                                  moyennePhysique= col_character(),
                                  sexe= col_character(),
                                  dateNaissance= col_character(),
                                  pcs=col_integer()
                                )
)



notesElevesMatières$dateNaissance<-as.Date(notesElevesMatières$dateNaissance,'%d%m%Y')
