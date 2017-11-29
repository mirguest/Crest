/*
 * CrestDB REST API
 * Crest Rest Api to manage data for calibration files.
 *
 * OpenAPI spec version: 2.0
 * Contact: andrea.formica@cern.ch
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package hep.crest.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import javax.validation.constraints.*;

/**
 * PayloadTagInfoDto
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaJerseyServerCodegen", date = "2017-11-23T12:27:33.393+01:00")
public class PayloadTagInfoDto   {
  @JsonProperty("tagname")
  private String tagname = null;

  @JsonProperty("niovs")
  private Integer niovs = null;

  @JsonProperty("totvolume")
  private Float totvolume = null;

  @JsonProperty("avgvolume")
  private Float avgvolume = null;

  public PayloadTagInfoDto tagname(String tagname) {
    this.tagname = tagname;
    return this;
  }

   /**
   * Get tagname
   * @return tagname
  **/
  @JsonProperty("tagname")
  @ApiModelProperty(value = "")
  public String getTagname() {
    return tagname;
  }

  public void setTagname(String tagname) {
    this.tagname = tagname;
  }

  public PayloadTagInfoDto niovs(Integer niovs) {
    this.niovs = niovs;
    return this;
  }

   /**
   * Get niovs
   * @return niovs
  **/
  @JsonProperty("niovs")
  @ApiModelProperty(value = "")
  public Integer getNiovs() {
    return niovs;
  }

  public void setNiovs(Integer niovs) {
    this.niovs = niovs;
  }

  public PayloadTagInfoDto totvolume(Float totvolume) {
    this.totvolume = totvolume;
    return this;
  }

   /**
   * Get totvolume
   * @return totvolume
  **/
  @JsonProperty("totvolume")
  @ApiModelProperty(value = "")
  public Float getTotvolume() {
    return totvolume;
  }

  public void setTotvolume(Float totvolume) {
    this.totvolume = totvolume;
  }

  public PayloadTagInfoDto avgvolume(Float avgvolume) {
    this.avgvolume = avgvolume;
    return this;
  }

   /**
   * Get avgvolume
   * @return avgvolume
  **/
  @JsonProperty("avgvolume")
  @ApiModelProperty(value = "")
  public Float getAvgvolume() {
    return avgvolume;
  }

  public void setAvgvolume(Float avgvolume) {
    this.avgvolume = avgvolume;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PayloadTagInfoDto payloadTagInfoDto = (PayloadTagInfoDto) o;
    return Objects.equals(this.tagname, payloadTagInfoDto.tagname) &&
        Objects.equals(this.niovs, payloadTagInfoDto.niovs) &&
        Objects.equals(this.totvolume, payloadTagInfoDto.totvolume) &&
        Objects.equals(this.avgvolume, payloadTagInfoDto.avgvolume);
  }

  @Override
  public int hashCode() {
    return Objects.hash(tagname, niovs, totvolume, avgvolume);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PayloadTagInfoDto {\n");
    
    sb.append("    tagname: ").append(toIndentedString(tagname)).append("\n");
    sb.append("    niovs: ").append(toIndentedString(niovs)).append("\n");
    sb.append("    totvolume: ").append(toIndentedString(totvolume)).append("\n");
    sb.append("    avgvolume: ").append(toIndentedString(avgvolume)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}
