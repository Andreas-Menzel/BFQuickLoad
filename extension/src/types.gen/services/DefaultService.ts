/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Preset } from '../models/Preset';
import type { PresetsCatalog } from '../models/PresetsCatalog';
import type { SearchFilter } from '../models/SearchFilter';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class DefaultService {
    /**
     * Ping
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getPing(): CancelablePromise<any> {
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
     * @returns PresetsCatalog Successful Response
     * @throws ApiError
     */
    public static getPresetsCatalog(): CancelablePromise<PresetsCatalog> {
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
    /**
     * Read Search Filters
     * @returns SearchFilter Successful Response
     * @throws ApiError
     */
    public static getAllSearchFilters(): CancelablePromise<Array<SearchFilter>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/search_filters',
        });
    }
    /**
     * Read Search Filter
     * @param filterId
     * @returns SearchFilter Successful Response
     * @throws ApiError
     */
    public static getSearchFilter(
        filterId: number,
    ): CancelablePromise<SearchFilter> {
        return __request(OpenAPI, {
            method: 'GET',
            url: 'search_filter/{filter_id}',
            path: {
                'filter_id': filterId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
