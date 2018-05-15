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
 * FolderDto
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaJerseyServerCodegen", date = "2018-05-10T14:37:32.399+02:00")
public class FolderDto   {
  @JsonProperty("nodeFullpath")
  private String nodeFullpath = null;

  @JsonProperty("schemaName")
  private String schemaName = null;

  @JsonProperty("nodeName")
  private String nodeName = null;

  @JsonProperty("nodeDescription")
  private String nodeDescription = null;

  @JsonProperty("tagPattern")
  private String tagPattern = null;

  @JsonProperty("groupRole")
  private String groupRole = null;

  public FolderDto nodeFullpath(String nodeFullpath) {
    this.nodeFullpath = nodeFullpath;
    return this;
  }

  /**
   * Get nodeFullpath
   * @return nodeFullpath
   **/
  @JsonProperty("nodeFullpath")
  @ApiModelProperty(value = "")
  public String getNodeFullpath() {
    return nodeFullpath;
  }

  public void setNodeFullpath(String nodeFullpath) {
    this.nodeFullpath = nodeFullpath;
  }

  public FolderDto schemaName(String schemaName) {
    this.schemaName = schemaName;
    return this;
  }

  /**
   * Get schemaName
   * @return schemaName
   **/
  @JsonProperty("schemaName")
  @ApiModelProperty(value = "")
  public String getSchemaName() {
    return schemaName;
  }

  public void setSchemaName(String schemaName) {
    this.schemaName = schemaName;
  }

  public FolderDto nodeName(String nodeName) {
    this.nodeName = nodeName;
    return this;
  }

  /**
   * Get nodeName
   * @return nodeName
   **/
  @JsonProperty("nodeName")
  @ApiModelProperty(value = "")
  public String getNodeName() {
    return nodeName;
  }

  public void setNodeName(String nodeName) {
    this.nodeName = nodeName;
  }

  public FolderDto nodeDescription(String nodeDescription) {
    this.nodeDescription = nodeDescription;
    return this;
  }

  /**
   * Get nodeDescription
   * @return nodeDescription
   **/
  @JsonProperty("nodeDescription")
  @ApiModelProperty(value = "")
  public String getNodeDescription() {
    return nodeDescription;
  }

  public void setNodeDescription(String nodeDescription) {
    this.nodeDescription = nodeDescription;
  }

  public FolderDto tagPattern(String tagPattern) {
    this.tagPattern = tagPattern;
    return this;
  }

  /**
   * Get tagPattern
   * @return tagPattern
   **/
  @JsonProperty("tagPattern")
  @ApiModelProperty(value = "")
  public String getTagPattern() {
    return tagPattern;
  }

  public void setTagPattern(String tagPattern) {
    this.tagPattern = tagPattern;
  }

  public FolderDto groupRole(String groupRole) {
    this.groupRole = groupRole;
    return this;
  }

  /**
   * Get groupRole
   * @return groupRole
   **/
  @JsonProperty("groupRole")
  @ApiModelProperty(value = "")
  public String getGroupRole() {
    return groupRole;
  }

  public void setGroupRole(String groupRole) {
    this.groupRole = groupRole;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FolderDto folderDto = (FolderDto) o;
    return Objects.equals(this.nodeFullpath, folderDto.nodeFullpath) &&
        Objects.equals(this.schemaName, folderDto.schemaName) &&
        Objects.equals(this.nodeName, folderDto.nodeName) &&
        Objects.equals(this.nodeDescription, folderDto.nodeDescription) &&
        Objects.equals(this.tagPattern, folderDto.tagPattern) &&
        Objects.equals(this.groupRole, folderDto.groupRole);
  }

  @Override
  public int hashCode() {
    return Objects.hash(nodeFullpath, schemaName, nodeName, nodeDescription, tagPattern, groupRole);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FolderDto {\n");
    
    sb.append("    nodeFullpath: ").append(toIndentedString(nodeFullpath)).append("\n");
    sb.append("    schemaName: ").append(toIndentedString(schemaName)).append("\n");
    sb.append("    nodeName: ").append(toIndentedString(nodeName)).append("\n");
    sb.append("    nodeDescription: ").append(toIndentedString(nodeDescription)).append("\n");
    sb.append("    tagPattern: ").append(toIndentedString(tagPattern)).append("\n");
    sb.append("    groupRole: ").append(toIndentedString(groupRole)).append("\n");
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
