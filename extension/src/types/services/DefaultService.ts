/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Preset } from '../models/Preset';
import type { PresetMetadata } from '../models/PresetMetadata';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class DefaultService {
    /**
     * Ping
     * @returns any Successful Response
     * @throws ApiError
     */
    public static ping(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/ping',
        });
    }
    /**
     * Read Root
     * @returns any Successful Response
     * @throws ApiError
     */
    public static readRootGet(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/',
        });
    }
    /**
     * Read Catalog
     * @returns PresetMetadata Successful Response
     * @throws ApiError
     */
    public static getCatalog(): CancelablePromise<Array<PresetMetadata>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/presets/catalog',
        });
    }
    /**
     * Read Presets
     * @returns Preset Successful Response
     * @throws ApiError
     */
    public static getAllPresets(): CancelablePromise<Array<Preset>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/presets',
        });
    }
    /**
     * Read Preset
     * @param presetId
     * @returns Preset Successful Response
     * @throws ApiError
     */
    public static getPreset(
        presetId: number,
    ): CancelablePromise<Preset> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/presets/{preset_id}',
            path: {
                'preset_id': presetId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
