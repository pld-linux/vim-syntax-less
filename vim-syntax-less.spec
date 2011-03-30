%define		syntax	less
Summary:	Vim syntax: %{syntax}
Name:		vim-syntax-%{syntax}
Version:	0.1
Release:	1
License:	Charityware
Group:		Applications/Editors/Vim
Source0:	http://leafo.net/lessphp/vim/less.vim
# Source0-md5:	04261b795d7cbe1ff52904dda61fd1f6
Source1:	http://leafo.net/lessphp/vim/INSTALL
# Source1-md5:	cdb67ffefd4f1d19bd87e67f7c9b0c0b
Source2:	ftdetect.vim
URL:		http://leafo.net/lessphp/vim/
# for _vimdatadir existence
Requires:	vim-rt >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
This plugin provides syntax highlighting for bacula config files.

%prep
%setup -qcT
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
cp -a %{syntax}.vim $RPM_BUILD_ROOT%{_vimdatadir}/syntax/%{syntax}.vim
cp -a ftdetect.vim $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{syntax}.vim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL
%{_vimdatadir}/syntax/%{syntax}.vim
%{_vimdatadir}/ftdetect/%{syntax}.vim
