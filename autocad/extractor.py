"""
File: extractor.py
Description: Extracts the attributes if the dwg file is dxf format.
Author: Its Me Hara
Date: Jan 05, 2024
Notes:
    This file contains the implementation of extracting dxf format dwg file. usually dwg file is autocad dwg file.
"""
import ezdxf
from utils.logger_utils import get_logger
from datetime import datetime
import pandas as pd

log = get_logger()


def get_output_csv(file_path, f_type="csv"):
    dt_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_csv = str(file_path.split(".")[0]) + f"_{dt_str}.{f_type}"
    # log.info(output_csv, file_path)
    return output_csv


def extract_parameters(file_path):
    doc = ezdxf.readfile(file_path)

    doc_has = [ item for item in dir(doc) ]
    log.info(f"{doc_has}")

    try:
        # Logic for extracting parameters from AutoCAD DWG files
        csv_file = get_output_csv(file_path)
        with open(csv_file, "w") as fp:
            # Sample: Extract and log layers
            lines = [["Layer", "linetype", "lineweight", "material_handle", "name", "owner", "plot", "plotstyle_handle"]]
            for layer in doc.layers:
                log.info(f"Layer: {layer.dxf.name}, linetype : {layer.dxf.linetype}, lineweight: {layer.dxf.lineweight}, ")
                log.info(f"material_handle: {layer.dxf.material_handle}, name: {layer.dxf.name}, owner : {layer.dxf.owner}, ")
                log.info(f"plot: {layer.dxf.plot}, plotstyle_handle: {layer.dxf.plotstyle_handle}, ")
                line = [layer.dxf.name, layer.dxf.linetype, layer.dxf.lineweight, layer.dxf.material_handle, layer.dxf.name,
                        layer.dxf.owner, layer.dxf.plot, layer.dxf.plotstyle_handle]
                lines.append(line)
            str_lines = "\n".join([str(l)[1:-1] for l in lines])
            fp.writelines(str_lines)
        # Add more extraction logic based on your project's requirements

        entities = list(doc.modelspace().query('*'))
        for entity in entities:
            # log.info(f"Entity Type: {entity.dxftype()} | Layer: {entity.dxf.layer} | Color: {entity.dxf.color} | params: {dir(entity.dxf.layer)}")
            log.info(f"Entity Type: {entity.dxftype()} | Layer: {entity.dxf.layer} | Color: {entity.dxf.color} ")

        texts = list(doc.modelspace().query('TEXT'))
        for text in texts:
            log.info(f"Text Content: {text.dxf.text}")

        block_references = list(doc.modelspace().query('INSERT'))
        for block_ref in block_references:
            log.info(f"Block Name: {block_ref.dxf.name}, dxfattribs : {block_ref.dxfattribs}")
            log.info(f"dxftype: {block_ref.dxftype}")

        block_references_with_attributes = list(doc.modelspace().query('INSERT:has(attribute)'))
        for block_ref in block_references_with_attributes:
            for attrib in block_ref.attribs():
                print(1)
                log.info(f"Attribute Value: {attrib.dxf.text}")
    except Exception as e:
        log.error("Error extracting parameters: %s", str(e))

    try:
        log.info("V^"*100)

        for block_ref in doc.modelspace().query('INSERT'):
            pass
            # log.info(dir(block_ref.dxf))
            # if "CHAIR" in block_ref.dxf.name:
            #     log.info(f"Block Name: {block_ref.dxf.name}")
            #
            #     for entity in block_ref.virtual_entities():
            #         log.info(f"Entity Type: {entity.dxftype()}")
            #         log.info(f"Layer: {entity.dxf.layer}")
            #         log.info(f"Color: {entity.dxf.color}")
            #         log.info(f"Linetype: {entity.dxf.linetype}")
            #         log.info(f"Lineweight: {entity.dxf.lineweight}")
            #         log.info(f"Material: {entity.dxf.material_handle}")
            #         log.info(f"Visibility: {entity.dxf.get('visibility', True)}")
            #         log.info(f"Scale Factors: X={entity.dxf.get('xscale', 1.0)}, Y={entity.dxf.get('yscale', 1.0)}, Z={entity.dxf.get('zscale', 1.0)}")
            #         log.info("-" * 30)

    except Exception as e:
        log.error("Error extracting parameters: %s", str(e))


def extract_parameters_excel(file_path):
    try:
        # Logic for extracting parameters from AutoCAD DWG files
        doc = ezdxf.readfile(file_path)
        excel_file = get_output_csv(file_path, "xlsx")
        # Assuming doc.layers is a list of layer objects

        # Create a DataFrame with layer information
        data = []
        for layer in doc.layers:
            data.append([layer.dxf.name, layer.dxf.linetype, layer.dxf.lineweight, layer.dxf.material_handle,
                         layer.dxf.owner, layer.dxf.plot, layer.dxf.plotstyle_handle])

        df = pd.DataFrame(data, columns=["Layer", "linetype", "lineweight", "material_handle",
                                         "owner", "plot", "plotstyle_handle"])

        # Write the DataFrame to an Excel file
        df.to_excel(excel_file, index=False)

    except Exception as e:
        log.error("Error extracting parameters: %s", str(e))
