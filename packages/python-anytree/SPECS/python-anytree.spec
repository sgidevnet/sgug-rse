%global modname anytree

Name:           python-anytree
Version:        2.8.0
Release:        2%{?dist}
Summary:        Powerful and Lightweight Python Tree Data Structure

License:        ASL 2.0
URL:            https://pypi.io/project/anytree
Source0:        %pypi_source %{modname}

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
# Prohibit that the file LICENSE will be installed in usr from the python setup
sed -e "/LICENSE/d" -i setup.py


%build
%py3_build


%install
%py3_install


%files -n python3-anytree
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*


%changelog
* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 2.8.0-2
- Rebuilt for Python 3.9

* Fri Mar 06 2020 Gerd Pokorra <gz@zimt.uni-siegen.de> - 2.8.0-1
- The sources now has the license file included

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 03 2019 Lubomir Rintel <lkundrak@v3.sk> - 2.7.2-2
- Fixes suggested in a review from Elliott Sales de Andrade (#1768186):
- Fix the license file location
- Tag the license file appropriately
- Use the apppropriate python build tags

* Sun Nov 03 2019 Lubomir Rintel <lkundrak@v3.sk> - 2.7.2-1
- Initial packaging
