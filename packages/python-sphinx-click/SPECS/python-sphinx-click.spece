%global pypi_name sphinx-click

Name:           python-%{pypi_name}
Version:        2.3.2
Release:        2%{?dist}
Summary:        Sphinx extension that automatically documents Click applications

License:        MIT
URL:            https://github.com/click-contrib/sphinx-click/
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(pbr) >= 2
BuildRequires:  python3dist(sphinx)

%global package_desc \
sphinx-click is a Sphinx plugin that allows you to automatically extract\
documentation from a click-based application and include it in your docs.

%description
%{package_desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{package_desc}

%package -n python-%{pypi_name}-doc
Summary:        Documentation for sphinx-click
%description -n python-%{pypi_name}-doc
Documentation for sphinx-click

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# No coverage check needed
sed -i '/coverage/d' test-requirements.txt


%build
%py3_build
# generate html docs 
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinx_click/
%{python3_sitelib}/sphinx_click-%{version}-py?.?.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Charalampos Stratakis <cstratak@redhat.com> - 2.3.2-1
- Update to 2.3.2 (#1822901)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-1
- Update to 2.3.1 (#1754192)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-1
- Update to 2.2.0 for Sphinx 2.1 official support (#1704910)

* Wed Mar 13 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- sphinx-click 2.0.1 works with sphinx 2.0.0b1

* Sun Feb 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-1
- Update to 2.0.1 to make it build with Click 7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-2
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Michal Cyprian <mcyprian@redhat.com> - 1.0.4-1
- Initial package.
