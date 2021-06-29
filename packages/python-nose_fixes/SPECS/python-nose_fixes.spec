
%global pypi_name nose_fixes
%global global_sum Plugin to make nose behave better
%global global_desc A plugin that changes nose to behave better.


Name:		python-%{pypi_name}
Version:	1.3
Release:	9%{?dist}
Summary:	%{global_sum}

License:	MIT
URL:		https://pypi.python.org/pypi/%{pypi_name}
Source0:	https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:	noarch

%description
%{global_desc}


%package doc
Summary:	Documentation-files for %{name}

%description doc
This package contains the documentation-files for %{name}.


%package -n python3-%{pypi_name}
Summary:	%{global_sum}

BuildRequires:	python3-devel
BuildRequires:	python3-nose
BuildRequires:	python3-pkginfo
BuildRequires:	python3-setuptools
BuildRequires:	python3-sphinx

Requires:	python3-nose

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{global_desc}


%prep
%autosetup -n %{pypi_name}-%{version}
%{__rm} -fr *.egg*
%{__sed} -i -e 's!^SPHINXBUILD[ \t]*=.*$!SPHINXBUILD = %{_bindir}/sphinx-build!g' docs/Makefile


%build
%py3_build
%{__make} -C docs html


%install
%py3_install
%{__rm} -f docs/_build/html/{.buildinfo,objects.inv}


%check
%{_bindir}/nosetests-%{python3_version} -vv


%files doc
%doc docs/changes.txt docs/_build/html PKG-INFO
%license docs/license.txt


%files -n python3-%{pypi_name}
%doc PKG-INFO
%license docs/license.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-8
- Subpackage python2-nose_fixes has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3-5
- Rebuilt for Python 3.7

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 26 2017 Björn Esser <besser82@fedoraproject.org> - 1.3-1
- Initial import (rhbz#1445822)

* Wed Apr 26 2017 Björn Esser <besser82@fedoraproject.org> - 1.3-0.1
- Initial rpm-release (rhbz#1445822)
