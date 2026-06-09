package com.momopdf.app

import android.Manifest
import android.annotation.SuppressLint
import android.app.Activity
import android.app.DownloadManager
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Bundle
import android.os.Environment
import android.webkit.CookieManager
import android.webkit.DownloadListener
import android.webkit.URLUtil
import android.webkit.ValueCallback
import android.webkit.WebChromeClient
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat

class MainActivity : AppCompatActivity() {

    private lateinit var webView: WebView
    private var filePathCallback: ValueCallback<Array<Uri>>? = null
    private val FILE_CHOOSER_RESULT_CODE = 1
    private val STORAGE_PERMISSION_CODE = 101

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        webView = WebView(this)
        setContentView(webView)

        setupWebView()
        checkStoragePermissions()
        
        webView.loadUrl("https://13.48.78.233.nip.io") 
    }

    private fun setupWebView() {
        val webSettings: WebSettings = webView.settings
        webSettings.javaScriptEnabled = true
        webSettings.domStorageEnabled = true
        webSettings.allowFileAccess = true
        webSettings.allowContentAccess = true

        webView.webViewClient = object : WebViewClient() {
            override fun shouldOverrideUrlLoading(view: WebView?, url: String?): Boolean {
                if (url != null && url.startsWith("https://")) {
                    view?.loadUrl(url)
                    return true
                }
                return false
            }
        }

        webView.webChromeClient = object : WebChromeClient() {
            override fun onShowFileChooser(
                webView: WebView?,
                filePathCallback: ValueCallback<Array<Uri>>?,
                fileChooserParams: FileChooserParams?
            ): Boolean {
                this@MainActivity.filePathCallback = filePathCallback
                val intent = Intent(Intent.ACTION_GET_CONTENT)
                intent.addCategory(Intent.CATEGORY_OPENABLE)
                intent.type = "*/*"
                startActivityForResult(Intent.createChooser(intent, "File Chooser"), FILE_CHOOSER_RESULT_CODE)
                return true
            }
        }

        webView.setDownloadListener { url, userAgent, contentDisposition, mimetype, contentLength ->
            downloadFile(url, userAgent, contentDisposition, mimetype)
        }
    }

    private fun downloadFile(url: String, userAgent: String, contentDisposition: String, mimeType: String) {
        val request = DownloadManager.Request(Uri.parse(url))
        val filename = URLUtil.guessFileName(url, contentDisposition, mimeType)
        val cookies = CookieManager.getInstance().getCookie(url)
        
        request.setMimeType(mimeType)
        request.addRequestHeader("cookie", cookies)
        request.addRequestHeader("User-Agent", userAgent)
        request.setDescription("Downloading file...")
        request.setTitle(filename)
        request.allowScanningByMediaScanner()
        request.setNotificationVisibility(DownloadManager.Request.VISIBILITY_VISIBLE_NOTIFY_COMPLETED)
        request.setDestinationInExternalPublicDir(Environment.DIRECTORY_DOWNLOADS, "momopdf/$filename")

        val dm = getSystemService(Context.DOWNLOAD_SERVICE) as DownloadManager
        dm.enqueue(request)
        Toast.makeText(applicationContext, "Downloading File", Toast.LENGTH_LONG).show()
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        if (requestCode == FILE_CHOOSER_RESULT_CODE) {
            val result = if (data == null || resultCode != Activity.RESULT_OK) null else data.data
            if (result != null) {
                filePathCallback?.onReceiveValue(arrayOf(result))
            } else {
                filePathCallback?.onReceiveValue(null)
            }
            filePathCallback = null
        }
        super.onActivityResult(requestCode, resultCode, data)
    }

    private fun checkStoragePermissions() {
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.WRITE_EXTERNAL_STORAGE, Manifest.permission.READ_EXTERNAL_STORAGE), STORAGE_PERMISSION_CODE)
        }
    }

    override fun onBackPressed() {
        if (webView.canGoBack()) {
            webView.goBack()
        } else {
            super.onBackPressed()
        }
    }
}
