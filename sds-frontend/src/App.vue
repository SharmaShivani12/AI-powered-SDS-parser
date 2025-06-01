<template>
  <div class="container py-5">
    <h1 class="mb-4 text-primary fw-bold">🧪 SDS Parser App</h1>

    <!-- File Upload -->
    <form @submit.prevent="uploadFile" class="mb-4 row g-2 align-items-center">
      <div class="col-auto">
        <input type="file" @change="handleFileChange" class="form-control" accept=".pdf" />
      </div>
      <div class="col-auto">
        <button type="submit" class="btn btn-primary">Upload SDS PDF</button>
      </div>
    </form>

    <div v-if="uploadMessage" class="alert alert-info py-2">
      {{ uploadMessage }}
    </div>

    <!-- SDS Records -->
    <h2 class="h4 mb-3">Uploaded SDS Records</h2>

    <ul v-if="records.length" class="list-group">
      <li v-for="record in records" :key="record.id" class="list-group-item">
        <h5 class="fw-semibold">{{ record.product_name || 'Unnamed Product' }}</h5>
        <p class="mb-1">CAS: <strong>{{ record.cas_number || 'N/A' }}</strong></p>
        <p class="mb-0">Manufacturer: <strong>{{ record.manufacturer || 'N/A' }}</strong></p>
      </li>
    </ul>

    <div v-else class="text-muted">No records yet. Upload an SDS PDF to get started.</div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      selectedFile: null,
      uploadMessage: '',
      records: [],
    }
  },
  mounted() {
    this.fetchRecords()
  },
  methods: {
    handleFileChange(event) {
      this.selectedFile = event.target.files[0]
    },
    uploadFile() {
      if (!this.selectedFile) {
        this.uploadMessage = "Please select a PDF file first."
        return
      }

      const formData = new FormData()
      formData.append("file", this.selectedFile)

      axios.post("http://127.0.0.1:8000/api/upload/", formData)
        .then(() => {
          this.uploadMessage = "✅ Uploaded and parsed successfully!"
          this.selectedFile = null
          this.fetchRecords()
        })
        .catch(() => {
          this.uploadMessage = "❌ Upload failed. Try again."
        })
    },
    fetchRecords() {
      axios.get("http://127.0.0.1:8000/api/sds/")
        .then(res => this.records = res.data)
        .catch(err => console.error("Failed to fetch SDS records:", err))
    }
  }
}
</script>
