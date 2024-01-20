<!DOCTYPE html>
<html lang="en">
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

        <!-- FontAwesome Icons -->
    <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
    />

    <link rel="stylesheet" href="css/bannerCSS.css" />
    </head>
    <body>
        <input type="button" value="articles" class="directoryButton" onClick="document.location.href='articles/index.php'" />
        <input type="button" value="campaign" class="directoryButton" onClick="document.location.href='campaign/index.php'" />
        <input type="button" value="published" class="directoryButton" onClick="document.location.href='published/index.php'" />
        <!-- <input type="button" value="Old Website" class="directoryButton" onClick="document.location.href='OLD WEBSITE/index.php'" /> This is for referencing my old stuff -->
    </body>
        <?php include_once("inc/banner.php");?> <!-- "../inc/banner.php" for nested files -->
    <style>
        *{
            box-sizing:border-box;
        }

        input[type="button"]{
            margin-top: 100px;
        }
    </style>
</html>