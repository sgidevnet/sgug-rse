%global pypi_name PyDispatcher
%global srcname pydispatcher

Name:           python-%{srcname}
Version:        2.0.5
Release:        12%{?dist}
Summary:        Multi-producer-multi-consumer signal dispatching mechanism

License:        BSD
URL:            http://pydispatcher.sourceforge.net
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description Dispatcher mechanism for creating event models. \
PyDispatcher is an enhanced version of Patrick K. O'Brien's original \
dispatcher.py module. It provides the Python programmer with a robust \
mechanism for event routing within various application contexts. \
Included in the package are the `robustapply` and `saferef` modules, \
which provide the ability to selectively apply arguments to callable \
objects and to reference instance methods using weak-references.

%description
%{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}

This package contains the Python 3 version of %{pypi_name}.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test -s tests


%files -n python3-%{srcname}
%license license.txt
%doc PKG-INFO
%{python3_sitelib}/pydispatch
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-10
- Subpackage python2-pydispatcher has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 05 2017 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.5-1
- Initial package.
