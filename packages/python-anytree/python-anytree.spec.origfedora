%global modname anytree

Name:           python-anytree
Version:        2.7.2
Release:        1%{?dist}
Summary:        Powerful and Lightweight Python Tree Data Structure

License:        ASL 2.0
URL:            https://pypi.io/project/anytree
Source0:        %pypi_source %{modname}
# This is missing from the source tree: https://github.com/c0fec0de/anytree/pull/104
Source1:        https://raw.githubusercontent.com/c0fec0de/anytree/%{version}/LICENSE#/%{name}-LICENSE

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Powerful and Lightweight Python Tree Data Structure with various plugins.


%package -n python3-anytree
Summary:        Powerful and Lightweight Python Tree Data Structure

%description -n python3-anytree
Powerful and Lightweight Python Tree Data Structure with various plugins.

%prep
%setup -q -n %{modname}-%{version}
rm -r %{modname}.egg-info
install -pm644 %{SOURCE1} LICENSE


%build
%py3_build


%install
%py3_install


%files -n python3-anytree
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*
%doc README.rst
%license LICENSE


%changelog
* Fri Mar 06 2020 Gerd Pokorra <gz@zimt.uni-siegen.de> - 2.7.2-1
- This things are done by Lubomir Rintel <lkundrak@v3.sk>:
- Fixes suggested in a review from Elliott Sales de Andrade (#1768186):
- Fix the license file location
- Tag the license file appropriately
- Use the apppropriate python build tags
- Initial packaging
