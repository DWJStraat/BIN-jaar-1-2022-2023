subset(airquality, Temp<70, select = c(Ozone, Wind))

subset(airquality, Wind>12, select = c(Ozone, Wind))

subset(airquality, Day==1, select = c(Ozone, Temp, Day))

subset(airquality, Day==1, select = -c(Temp))

?airquality

airquality[,1:3]

airquality[8:14,]

dayofweek <- c("Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday")

airquality <- cbind(airquality, data.frame(dayofweek))

subset(airquality, dayofweek=="Sunday")

subset(airquality, is.na(Ozone))