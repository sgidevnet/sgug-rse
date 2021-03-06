%global pypi_name sphinxcontrib-htmlhelp

# when bootstrapping sphinx, we cannot run tests yet
%bcond_with check

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        2%{?dist}
Summary:        Sphinx extension for HTML help files
License:        BSD
URL:            http://sphinx-doc.org/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if %{with check}
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx >= 1:2
BuildRequires:  python3-html5lib
%endif

%description
sphinxcontrib-htmlhelp is a sphinx extension which renders HTML help files.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
sphinxcontrib-htmlhelp is a sphinx extension which renders HTML help files.


%prep
%autosetup -n %{pypi_name}-%{version}
find -name '*.mo' -delete


%build
for po in $(find -name '*.po'); do
  msgfmt --output-file=${po%.po}.mo ${po}
done
%py3_build


%install
%py3_install

# Move language files to /usr/share
export PREV_WD=`pwd`
cd %{buildroot}%{python3_sitelib}
for lang in `find sphinxcontrib/htmlhelp/locales -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -printf "%f "`;
do
  test $lang == __pycache__ && continue
  install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mv sphinxcontrib/htmlhelp/locales/$lang/LC_MESSAGES/*.mo %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
done
rm -rf sphinxcontrib/htmlhelp/locales
ln -s %{_datadir}/locale sphinxcontrib/htmlhelp/locales
cd $PREV_WD


%find_lang sphinxcontrib.htmlhelp


%if %{with check}
%check
%{__python3} -m pytest
%endif


%files -n python3-%{pypi_name} -f sphinxcontrib.htmlhelp.lang
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinxcontrib/
%{python3_sitelib}/sphinxcontrib_htmlhelp-%{version}-py%{python3_version}-*.pth
%{python3_sitelib}/sphinxcontrib_htmlhelp-%{version}-py%{python3_version}.egg-info/


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-1
- Initial package
