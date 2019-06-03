library(sqldf)
df1 <- sqldf("select * from mtcars where carb=1 order by mpg",
             row.names=TRUE)

df2<-sqldf("select avg(mpg) as avg_mpg, avg(disp) as avg_disp, gear
from mtcars where cyl in (4, 6) group by gear")