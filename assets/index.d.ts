import { GridApi, } from "ag-grid-enterprise";

declare global {
	namespace dash_ag_grid {
		export function getApi(s: String | Object): GridApi;
		export function getApiAsync(s: String | Object): Promise<GridApi>;
	}
	namespace dash_clientside {
		export const no_update: Object;
	}
}
export * from "ag-grid-enterprise";
