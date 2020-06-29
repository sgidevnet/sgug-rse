%global srcname geomet

Name:           python-%{srcname}
Version:        0.2.1
Release:        4%{?dist}
Summary:        GeoJSON <-> WKT/WKB conversion utilities

License:        ASL 2.0
URL:            https://github.com/geomet/geomet
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(nose)

%description
Convert GeoJSON to WKT/WKB (Well-Known Text/Binary), and vice versa.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Convert GeoJSON to WKT/WKB (Well-Known Text/Binary), and vice versa.


%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

# Remove unnecessary shebang
for file in geomet/tool.py; do
  sed -i.orig -e '1d' ${file} && \
  touch -r ${file}.orig ${file} && \
  rm ${file}.orig
done

# Allow Python 3.8
sed -i -e 's/, <3\.8//' setup.py


%build
%py3_build


%install
%py3_install

rm %{buildroot}%{_prefix}/LICENSE


%check
%{__python3} setup.py test


%files -n python3-%{srcname}
%license LICENSE
%{_bindir}/geomet
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 24 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-3.post2
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2.post2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-1.post2
- Initial package.
