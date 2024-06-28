<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);

    $mail = new PHPMailer(true);

    try {
        //Server settings
        $mail->SMTPDebug = 0;                                 
        $mail->isSMTP();                                      
        $mail->Host       = 'smtp.gmail.com';                 
        $mail->SMTPAuth   = true;                             
        $mail->Username   = 'your-email@gmail.com';           
        $mail->Password   = 'your-app-password';              
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;   
        $mail->Port       = 587;                              

        //Recipients
        $mail->setFrom('your-email@gmail.com', 'Mailer');
        $mail->addAddress('your-email@gmail.com', 'Joe User');

        //Content
        $mail->isHTML(true);                                  
        $mail->Subject = 'Yeni İletişim Formu Mesajı';
        $mail->Body    = "Ad: $name<br>Email: $email<br>Mesaj: $message";

        $mail->send();
        echo 'Mesaj gönderildi.';
    } catch (Exception $e) {
        echo "Mesaj gönderilemedi. Mailer Error: {$mail->ErrorInfo}";
    }
} else {
    echo '<form action="contact.php" method="POST">
        <label for="name">Adınız:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="message">Mesajınız:</label>
        <textarea id="message" name="message" required></textarea><br>
        <button type="submit">Gönder</button>
    </form>';
}
?>
