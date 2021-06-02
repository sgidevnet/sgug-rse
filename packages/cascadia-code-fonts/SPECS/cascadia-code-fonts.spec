%global fontname cascadia-code
%global fontconf 61-%{fontname}.conf

# We cannot build this from source until fontmake arrives in Fedora.
%global fromsource 0

Name:		%{fontname}-fonts
Summary:	A monospaced font designed for programming and terminal emulation
Version:	2009.22
Release:	1%{?dist}
License:	OFL
URL:		https://github.com/microsoft/cascadia-code/
Source0:	https://github.com/microsoft/cascadia-code/archive/v%{version}.tar.gz
Source1:	%{name}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml
%if 0%{?fromsource}
BuildRequires:	python3-fontmake
%else
Source3:	https://github.com/microsoft/cascadia-code/releases/download/v%{version}/CascadiaCode-%{version}.zip
%endif
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
Cascadia Code is a monospaced font designed to provide a fresh experience for
command line experiences and code editors. Notably, it supports programming
ligatures (except in the "Cascadia Mono" variant).

%prep
%setup -q -n %{fontname}-%{version}

# correct end-of-line encoding
for i in OFL-FAQ.txt FONTLOG.txt README.md; do
	sed -i 's/\r//' $i
done

%build

%if 0%{?fromsource}
python3 build.py
%else
unzip %{SOURCE3}
%endif

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p otf/static/*.otf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.otf
%license LICENSE
%doc FONTLOG.txt OFL-FAQ.txt README.md
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Thu Sep 24 2020 Tom Callaway <spot@fedoraproject.org> - 2009.22-1
- update to 2009.22

* Mon Sep 21 2020 Tom Callaway <spot@fedoraproject.org> - 2009.14-1
- update to 2009.14

* Wed Sep  2 2020 Tom Callaway <spot@fedoraproject.org> - 2008.25-1
- update to 2008.25

* Wed Jul  1 2020 Tom Callaway <spot@fedoraproject.org> - 2007.01-1
- update to 2007.01

* Mon May 18 2020 Tom Callaway <spot@fedoraproject.org> - 2005.15-1
- update to 2005.15
- switch to otf files

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1911.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec  3 2019 Tom Callaway <spot@fedoraproject.org> - 1911.21-1
- update to 1911.21

* Wed Nov 13 2019 Tom Callaway <spot@fedoraproject.org> - 1910.04-1
- update to 1910.04

* Thu Sep 19 2019 Tom Callaway <spot@fedoraproject.org> - 1909.16-1
- initial package
