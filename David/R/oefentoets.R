? iris
summary(iris)

versicolor <- iris[iris$Species == "versicolor",]
summary(versicolor)

setosa <- iris[iris$Species == "setosa",]
boxplot(setosa$Sepal.Length, setosa$Sepal.Width, setosa$Petal.Length, setosa$Petal.Width, names = c("Sepal.Length",
                                                                                                    "Sepal.Width",
                                                                                                    "Petal.Length",
                                                                                                    "Petal.Width"),
        main = "Setosa")

versicolor <- iris[iris$Species == "versicolor",]
setosa <- iris[iris$Species == "setosa",]
virginica <- iris[iris$Species == "virginica",]
plot(virginica$Petal.Length, virginica$Petal.Width, xlim = c(0, 8), ylim = c(0, 3),
     main = "Virginica", sub = "bron: irisdataset van Fisher", xlab = "Petal Length", ylab = "Petal Width", col = "red")
points(versicolor$Petal.Length, versicolor$Petal.Width, col = "blue")
points(setosa$Petal.Length, setosa$Petal.Width, col = "green")
legend("topleft", legend = c("setosa", "versicolor", "virginica"), col = c("green", "blue", "red"), pch = 1)